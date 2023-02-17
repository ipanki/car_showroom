from django.db.models import Sum

from applications.history.models import SellHistory


def get_summary_report(pk):
    stats = SellHistory.objects.filter(car_showroom__id=pk).values(
        'car', 'car_showroom', 'price').annotate(amount_cars=Sum('count'), amount=Sum('price'))
    return stats
