from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from applications.extensions.abstract_models import AbstractInstance


class Supplier(AbstractInstance):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="suppliers")
    name = models.CharField(max_length=40)
    description = models.CharField(blank=True, max_length=200)
    found_year = models.DateField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=True)


class CarSupplier(AbstractInstance):
    count = models.PositiveIntegerField(default=1)
    car = models.ForeignKey(
        'car.Car', on_delete=models.SET_NULL, related_name='cars_in_stock', null=True)
    supplier = models.ForeignKey(
        'supplier.Supplier', on_delete=models.CASCADE, related_name='supplier_cars', null=True)


class SupplierSale(AbstractInstance):
    car = models.ForeignKey(
        'car.Car', on_delete=models.CASCADE, related_name='cars_sale', null=True)
    end_date = models.DateField(blank=True)
    supplier = models.ForeignKey(
        'supplier.Supplier', on_delete=models.CASCADE, related_name='supplier_sale', null=True)
    discount = models.IntegerField(validators=[MaxValueValidator(100),
                                               MinValueValidator(0)])
