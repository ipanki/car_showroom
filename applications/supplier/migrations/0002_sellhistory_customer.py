# Generated by Django 4.1.5 on 2023-01-30 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_delete_purchasehistory'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellhistory',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer'),
        ),
    ]
