from django.contrib import admin

from applications.car_showroom_app.models import CarsShowroom, Showroom


@admin.register(Showroom)
class ShowroomAdmin(admin.ModelAdmin):
    field = ('preferred_cars',)
    list_display = ('name', 'get_pref_car', 'balance', 'user')

    @staticmethod
    def get_pref_car(obj):
        return '\n'.join([p.color for p in obj.preferred_cars.all()])


@admin.register(CarsShowroom)
class CarsShowroomAdmin(admin.ModelAdmin):
    list_display = ('cars_showroom', 'car_showroom', 'count')
