from django.db.models import F, Q

from applications.car.models import CarPrice
from applications.car_showroom_app.models import CarShowroomSale, CarsShowroom
from applications.customer.models import Customer, Offer
from applications.history.models import SellHistory
from car_showroom.celery import app


@app.task
def customer_buy_cars():
    for customer in Customer.objects.all():
        for offer in Offer.objects.filter(customer=customer):
            showrooms_cars = CarsShowroom.objects.filter(
                Q(count__gte=1) & Q(cars_showroom=offer.car)).first()

            if showrooms_cars:
                car_price = CarPrice.objects.filter(Q(car=showrooms_cars.cars_showroom) &
                                                    Q(price__lte=offer.price)).order_by("-price").first()
            cars_on_discount = CarShowroomSale.objects.filter(
                car=offer.car).order_by("-discount").first()
            if cars_on_discount:
                car_price_on_discount = CarPrice.objects.filter(Q(car=cars_on_discount.car) &
                                                                Q(price__lte=offer.price)).order_by("-price").first()

            if showrooms_cars is None and cars_on_discount is None:
                continue
            elif showrooms_cars is None:
                purchase = cars_on_discount
                price = car_price_on_discount
            elif cars_on_discount is None:
                purchase = showrooms_cars
                price = car_price
            elif car_price_on_discount - car_price_on_discount * cars_on_discount.discount/100 > car_price.price:
                purchase = showrooms_cars
                price = car_price
            else:
                purchase = cars_on_discount
                price = car_price_on_discount

            if customer.balance >= price.price:
                customer.balance -= price.price
                purchase.car_showroom.balance += price.price

                CarsShowroom.objects.filter(
                    cars_showroom=purchase.cars_showroom, car_showroom=purchase.car_showroom).update(count=F('count') - 1)
                history = SellHistory.objects.create(
                    car_showroom=purchase.car_showroom, customer=customer, car=purchase.cars_showroom, price=price.price)
                history.save()
                purchase.car_showroom.save()
                customer.save()
