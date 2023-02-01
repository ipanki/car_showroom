from django.db import models
from applications.extensions.abstract_models import AbstractInstance


class SellHistory(AbstractInstance):
    supplier = models.ForeignKey('supplier.Supplier', on_delete=models.SET_NULL, null=True, related_name='history_supplier')
    customer = models.ForeignKey('customer.Customer', on_delete=models.SET_NULL, null=True, related_name='history_customer')
    car = models.ForeignKey('car.Car', on_delete=models.SET_NULL, null=True, related_name='history_car')
    car_showroom = models.ForeignKey('car_showroom_app.Showroom', on_delete=models.SET_NULL, null=True, related_name='history_showroom')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField(default=1)
