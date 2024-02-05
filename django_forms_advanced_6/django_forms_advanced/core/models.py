from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from django_forms_advanced.core.validators import validate_name


class UserModel(models.Model):
    MAX_NAME_LENGTH = 30
    MIN_FIRST_NAME_LENGTH = 2
    MIN_LAST_NAME_LENGTH = 4

    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_FIRST_NAME_LENGTH),
            validate_name,
        ),
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_LAST_NAME_LENGTH),
            validate_name,
        ),
    )

    age = models.PositiveIntegerField()

    user_profile_image = models.ImageField(
        upload_to="core/users_profile_images",
        null=True,
        blank=True,
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
    )