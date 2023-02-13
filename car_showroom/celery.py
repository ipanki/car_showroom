import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_showroom.settings')
app = Celery('car_showroom')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'buy-car-showroom-every-10-minute': {
        'task': 'applications.car_showroom_app.tasks.showroom_task',
        'schedule': crontab(minute='*/10'),
    },
    'customer-buy-car-every-minute': {
        'task': 'applications.customer.tasks.customer_task',
        'schedule': crontab(minute='*/1'),
    },
}
