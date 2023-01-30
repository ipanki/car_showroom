# Generated by Django 4.1.5 on 2023-01-30 10:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarShowroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CarShowroomSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('discount', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('start_time', models.DateField(auto_now_add=True)),
                ('end_time', models.DateField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CarsShowroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('count', models.PositiveIntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=20)),
                ('home', models.TextField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PreferredCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year', models.PositiveIntegerField()),
                ('car_showroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preferred_car_showroom', to='car_showroom_app.carshowroom')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]