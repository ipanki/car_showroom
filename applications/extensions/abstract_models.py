from django.db import models


class CreatedAt(models.Model):
    class Meta:
        abstract = True

    created_date = models.DateTimeField(auto_now_add=True)


class UpdatedAt(models.Model):
    class Meta:
        abstract = True

    updated_date = models.DateTimeField(auto_now=True)


class Delete(models.Model):
    class Meta:
        abstract = True

    is_active = models.BooleanField(default=True)
