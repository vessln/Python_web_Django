from django.core.validators import MinLengthValidator
from django.db import models


class TaskModel(models.Model):
    MAX_NAME_LENGTH = 15
    MIN_NAME_LENGTH = 5

    task_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=[MinLengthValidator(MIN_NAME_LENGTH), ],
        null=False,
        blank=False,
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    deadline = models.DateTimeField(
        null=False,
        blank=False,
    )





