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


class ReportRowSerializer(serializers.Serializer):
    car = serializers.IntegerField()
    car_showroom = serializers.IntegerField()
    count = serializers.IntegerField(source='amount_cars')
    price = serializers.DecimalField(decimal_places=2, max_digits=10)
    total = serializers.IntegerField(source='amount')


class ReportSerializer(serializers.Serializer):
    report = ReportRowSerializer(many=True)
