from django.db import models

from django_forms_basics.demoapp.validators import validator_only_letters_in_name


class Store(models.Model):
    shop_type = models.CharField(
        max_length=30,
    )

    def __str__(self):
        return self.shop_type


class Client(models.Model):
    MAX_LENGTH_NAME = 20
    TYPES = (
        (1, "male"),
        (2, "female"),
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
        validators=[validator_only_letters_in_name]
    )

    age = models.IntegerField(
        null=False,
        blank=False,
    )

    gender = models.IntegerField(
        choices=TYPES,
        null=False,
        blank=False,
    )

    shop = models.ForeignKey(
        to=Store,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )