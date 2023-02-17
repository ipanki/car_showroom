from rest_framework import serializers

from applications.car_showroom_app.models import Location
from applications.customer.models import Customer, Offer


class CreateCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('name', 'birthday', 'phone', 'location')


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('country', 'city', 'street', 'home')


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ('car', 'price', 'customer')


class ReportRowSerializer(serializers.Serializer):
    car = serializers.IntegerField()
    car_showroom = serializers.IntegerField()
    count = serializers.IntegerField()
    price = serializers.DecimalField(decimal_places=2, max_digits=10)


class ReportSerializer(serializers.Serializer):
    report = ReportRowSerializer(many=True)
