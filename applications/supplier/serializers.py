from rest_framework import serializers

from applications.car.serializers import CarSerializer
from applications.supplier.models import CarSupplier, Supplier, SupplierSale


class CreateSupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ('name', 'description', 'found_year')


class GetSupplierCarSerializer(serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = CarSupplier
        fields = ('count', 'car', 'supplier')


class SetSupplierSaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = SupplierSale
        fields = ('car', 'end_date', 'supplier', 'discount')
