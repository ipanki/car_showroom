from django.db import models
from applications.extensions.abstract_models import AbstractInstance


class CarConfiguration(AbstractInstance):
    description = models.TextField(blank=True)
    color = models.CharField(max_length=10)
    mileage = models.PositiveIntegerField(null=True, blank=True)
    year = models.PositiveIntegerField(blank=False)
    engine = models.DecimalField(max_digits=2, decimal_places=1)
    vin_number = models.CharField(max_length=17, unique=True)


class Car(AbstractInstance):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    car = models.OneToOneField('car.CarConfiguration', on_delete=models.CASCADE, blank=True, null=True, related_name='car_cfg')


class CarPrice(AbstractInstance):
    car = models.ForeignKey('car.Car', on_delete=models.CASCADE, related_name= 'car_prices')
    price = models.DecimalField(max_digits=10, decimal_places=2)
