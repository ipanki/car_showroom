# Generated by Django 4.1.6 on 2023-02-15 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car_showroom_app', '0001_initial'),
        ('supplier', '0001_initial'),
        ('car', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('count', models.PositiveIntegerField(default=1)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_car', to='car.car')),
                ('car_showroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_showroom', to='car_showroom_app.showroom')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_customer', to='customer.customer')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_supplier', to='supplier.supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
