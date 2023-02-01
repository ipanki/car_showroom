# Generated by Django 4.1.5 on 2023-01-30 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_showroom_app', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carsshowroom',
            name='supplier',
        ),
        migrations.AddField(
            model_name='carsshowroom',
            name='showroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='car_showroom_app.carshowroom'),
        ),
    ]