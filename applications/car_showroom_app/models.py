from django.db import models
from django.conf import settings
from applications.extensions.abstract_models import AbstractInstance
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField


class Location(AbstractInstance):
    country = CountryField()
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    home = models.TextField(max_length=10)


class Showroom(AbstractInstance):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="showroom_users")
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey('car_showroom_app.Location', on_delete=models.CASCADE, related_name='location')
    preferred_cars = models.ManyToManyField('car.CarConfiguration', null=True, blank=True, related_name='car_prefs')


class CarsShowroom(AbstractInstance):
    cars_showroom = models.ForeignKey('car.Car', on_delete=models.SET_NULL, null=True)
    count = models.PositiveIntegerField(default=1)
    car_showroom = models.ForeignKey('car_showroom_app.Showroom', on_delete=models.CASCADE, related_name="showroom_cars")


class CarShowroomSale(AbstractInstance):
    car = models.ForeignKey('car.Car', on_delete=models.CASCADE, related_name="car_on_sale")
    car_showroom = models.ForeignKey('car_showroom_app.Showroom', on_delete=models.CASCADE, related_name="showroom_sale")
    discount = models.IntegerField(validators=[MaxValueValidator(100),
                                               MinValueValidator(0)])
    start_time = models.DateField(auto_now_add=True)
    end_time = models.DateField(blank=True)


