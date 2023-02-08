from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models

from applications.extensions.abstract_models import AbstractInstance


class Customer(AbstractInstance):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="customers")
    name = models.CharField(max_length=50)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=40, validators=(
        RegexValidator(regex="^\+375[0-9]{2}[0-9]{7}$"),))
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    location = models.ForeignKey(
        'car_showroom_app.Location', on_delete=models.SET_NULL, null=True)


class Offer(AbstractInstance):
    car = models.ForeignKey(
        'car.Car', on_delete=models.CASCADE, related_name='offer_cars')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(
        'customer.Customer', on_delete=models.CASCADE, related_name='customer_offers')
