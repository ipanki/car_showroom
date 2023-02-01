from django.contrib import admin
from applications.car_showroom_app.models import Location
from applications.customer.models import Customer


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'home')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'birthday', 'balance', 'location')
