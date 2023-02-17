from applications.customer.services import customer_buy_cars
from car_showroom.celery import app


@app.task
def customer_task():
    customer_buy_cars.delay()
