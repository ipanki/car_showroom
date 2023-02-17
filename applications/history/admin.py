from django.contrib import admin

from applications.history.models import SellHistory


@admin.register(SellHistory)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'customer', 'car',
                    'car_showroom', 'price', 'count')
