from rest_framework import serializers

from applications.car_showroom_app.models import (CarShowroomSale,
                                                  CarsShowroom, Showroom)


class CreateShowroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Showroom
        fields = ('name', 'description', 'location', 'preferred_cars')


class GetShowroomCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarsShowroom
        fields = ('cars_showroom', 'count', 'car_showroom')


class SetShowroomSaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarShowroomSale
        fields = ('car', 'start_time', 'end_time', 'car_showroom', 'discount')


class ReportRowSerializer(serializers.Serializer):
    car = serializers.IntegerField()
    count = serializers.IntegerField(source='amount_cars')
    price = serializers.DecimalField(decimal_places=2, max_digits=10)
    total = serializers.IntegerField(source='amount')


class ReportSerializer(serializers.Serializer):
    expenses = ReportRowSerializer(many=True)
    incomes = ReportRowSerializer(many=True)
