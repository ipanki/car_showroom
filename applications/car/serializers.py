from rest_framework import serializers

from applications.car.models import Car, CarConfiguration, CarPrice


class CarConfigurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarConfiguration
        fields = ('description', 'color', 'mileage',
                  'year', 'engine', 'vin_number')


class CarSerializer(serializers.ModelSerializer):
    car = CarConfigurationSerializer()

    class Meta:
        model = Car
        fields = ('brand', 'model', 'car')


class SetCarPriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarPrice
        fields = ('car', 'price')
