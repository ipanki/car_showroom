from django.db import transaction
from django.db.models import F, Q, Sum

from applications.car.models import CarPrice
from applications.car_showroom_app.models import CarsShowroom, Showroom
from applications.history.models import SellHistory
from applications.supplier.models import CarSupplier, SupplierSale
from car_showroom.celery import app


@app.task
@transaction.atomic
def buy_cars():
    for showroom in Showroom.objects.prefetch_related('preferred_cars').all():
        for car_config in showroom.preferred_cars.all():
            pref_cars = (Q(car__car__color=car_config.color) &
                         Q(car__car__engine=car_config.engine) &
                         Q(car__car__mileage=car_config.mileage) &
                         Q(car__car__year=car_config.year))

            suppliers_cars = CarSupplier.objects.filter(pref_cars).first()
            if suppliers_cars:
                car_price = CarPrice.objects.filter(
                    pk=suppliers_cars.id).order_by("-price").first()
            cars_on_discount = SupplierSale.objects.filter(
                pref_cars).order_by("-discount").first()
            if cars_on_discount:
                car_price_on_discount = CarPrice.objects.filter(
                    pk=cars_on_discount.id).order_by("-price").first()

            if suppliers_cars is None and cars_on_discount is None:
                continue
            elif suppliers_cars is None:
                purchase = cars_on_discount
                price = car_price_on_discount
            elif cars_on_discount is None:
                purchase = suppliers_cars
                price = car_price
            elif car_price_on_discount - car_price_on_discount * cars_on_discount.discount/100 > car_price.price:
                purchase = suppliers_cars
                price = car_price
            else:
                purchase = cars_on_discount
                price = car_price_on_discount

            if showroom.balance >= price.price:
                showroom.balance -= price.price
                purchase.supplier.balance += price.price

                if CarsShowroom.objects.filter(cars_showroom=purchase.car, car_showroom=showroom).exists():
                    CarsShowroom.objects.filter(
                        cars_showroom=purchase.car, car_showroom=showroom).update(count=F('count') + 1)
                    history = SellHistory.objects.create(
                        supplier=purchase.supplier, car=purchase.car, car_showroom=showroom, price=price.price)
                    history.save()
                    showroom.save()
                    purchase.supplier.save()
                else:
                    purchased_car = CarsShowroom.objects.create(
                        cars_showroom=purchase.car, car_showroom=showroom)
                    history = SellHistory.objects.create(
                        supplier=purchase.supplier, car=purchase.car, car_showroom=showroom, price=price.price)
                    history.save()
                    purchased_car.save()
                    showroom.save()
                    purchase.supplier.save()


def get_summary_report(pk):
    stats = SellHistory.objects.filter(car_showroom__id=pk).values(
        'customer', 'car', 'price').annotate(amount_cars=Sum('count'), amount=Sum('price'))
    incomes = list(filter(lambda row: row['customer'], stats))
    expenses = list(filter(lambda row: not row['customer'], stats))
    return incomes, expenses
