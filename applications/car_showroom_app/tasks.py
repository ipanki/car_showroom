from car_showroom.celery import app
from applications.car_showroom_app.services import buy_cars


@app.task
def showroom_task():
    buy_cars.delay()
