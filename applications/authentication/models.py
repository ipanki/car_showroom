from authemail.models import EmailAbstractUser, EmailUserManager
from django.db import models


class User(EmailAbstractUser):
    class Roles(models.TextChoices):
        CUSTOMER = 'customer'
        SHOWROOM = 'showroom'
        SUPPLIER = 'supplier'

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=9, choices=Roles.choices, default=Roles.CUSTOMER)
    title = models.CharField(max_length=80)

    objects = EmailUserManager()

