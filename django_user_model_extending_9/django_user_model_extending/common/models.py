from django.contrib.auth import get_user_model
from django.db import models

from django_user_model_extending.accounts.models import Profile

UserModel = get_user_model()


class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Model1(AuditModel, models.Model):
    field = models.CharField(max_length=30)

    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.DO_NOTHING,
    # )
    # Example: request.user.model1_set()

    # WRONG way:
    # profile = models.ForeignKey(
    #     Profile,
    #     on_delete=models.DO_NOTHING,
    # )
    # Example: request.user.profile.model1_set()
