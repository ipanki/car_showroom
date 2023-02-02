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
