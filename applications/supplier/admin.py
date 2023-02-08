from django.contrib import admin

from applications.supplier.models import CarSupplier, Supplier


@admin.register(Supplier)
class CarAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'description', 'found_year', 'balance')


@admin.register(CarSupplier)
class CarAdmin(admin.ModelAdmin):
    list_display = ('count', 'car', 'supplier')
