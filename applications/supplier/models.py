from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from applications.extensions.abstract_models import CreatedAt, UpdatedAt, Delete


class Car(CreatedAt, UpdatedAt, Delete):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.PositiveIntegerField(null=True, blank=True)
    year = models.PositiveIntegerField(blank=False)
    vin_number = models.CharField(max_length=17, unique=True)


class Supplier(CreatedAt, UpdatedAt, Delete):
    name = models.CharField(max_length=40)
    description = models.CharField(blank=True, max_length=200)
    found_year = models.DateField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)


class CarSupplier(CreatedAt, UpdatedAt, Delete):
    count = models.PositiveIntegerField(default=1)
    car = models.ForeignKey('supplier.Car', on_delete=models.SET_NULL, related_name='cars_in_stock', null=True)
    supplier = models.ForeignKey('supplier.Supplier', on_delete=models.CASCADE, related_name='supplier_cars', null=True)


class SupplierSale(CreatedAt, UpdatedAt, Delete):
    car = models.ForeignKey('supplier.Car', on_delete=models.CASCADE, related_name='cars_sale', null=True)
    end_date = models.DateField(blank=True)
    supplier = models.ForeignKey('supplier.Supplier', on_delete=models.CASCADE, related_name='supplier_sale', null=True)
    discount = models.IntegerField(validators=[MaxValueValidator(100),
                                               MinValueValidator(0)])


class SellHistory(CreatedAt, UpdatedAt, Delete):
    supplier = models.ForeignKey('supplier.Supplier', on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    car_showroom = models.ForeignKey('car_showroom_app.CarShowroom', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField(default=1)
