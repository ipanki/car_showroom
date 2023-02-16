from django.contrib import admin

from applications.car_showroom_app.models import Location
from applications.customer.models import Customer, Offer


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'home')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'phone', 'birthday', 'balance', 'location', 'created_date')


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('car', 'price', 'customer')

