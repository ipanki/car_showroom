from django.db import models
from django.conf import settings
from applications.extensions.abstract_models import CreatedAt, UpdatedAt, Delete
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField


class Location(CreatedAt, UpdatedAt, Delete):
    country = CountryField()
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    home = models.TextField(max_length=10)


class CarShowroom(CreatedAt, UpdatedAt, Delete):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="showroom_users")
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey('car_showroom_app.Location', on_delete=models.CASCADE, related_name='location')


class CarsShowroom(CreatedAt, UpdatedAt, Delete):
    cars_showroom = models.ForeignKey('supplier.Car', on_delete=models.SET_NULL, null=True)
    count = models.PositiveIntegerField(default=1)
    car_showroom = models.ForeignKey('car_showroom_app.CarShowroom', on_delete=models.CASCADE, related_name="showroom_cars")


class CarShowroomSale(CreatedAt, UpdatedAt, Delete):
    car = models.ForeignKey('supplier.Car', on_delete=models.CASCADE, related_name="car_on_sale")
    car_showroom = models.ForeignKey('car_showroom_app.CarShowroom', on_delete=models.CASCADE, related_name="showroom_sale")
    discount = models.IntegerField(validators=[MaxValueValidator(100),
                                               MinValueValidator(0)])
    start_time = models.DateField(auto_now_add=True)
    end_time = models.DateField(blank=True)


class PreferredCar(CreatedAt, UpdatedAt, Delete):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveIntegerField(blank=False)

