from django.contrib import admin

from applications.car.models import Car, CarConfiguration, CarPrice


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'car')


@admin.register(CarConfiguration)
class CarConfigurationAdmin(admin.ModelAdmin):
    list_display = ('description', 'color', 'mileage',
                    'year', 'engine', 'vin_number')


@admin.register(CarPrice)
class CarPriceAdmin(admin.ModelAdmin):
    list_display = ('car', 'price')
