from applications.car_showroom_app.services import buy_cars
from car_showroom.celery import app


@app.task
def showroom_task():
    buy_cars.delay()
