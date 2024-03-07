from django.apps import apps
from django.contrib.auth.hashers import make_password

from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django.contrib import auth
from django.contrib.auth import base_user as auth_base

from django.contrib.auth import get_user_model, models as auth_models
from django.db import models


# 1. Use the default user.
# 2. Extend the AbstractUser class - extend the default user + add more stuff.
# 3. Extend the AbstractBaseUser class - rewrite the whole user.



# 1. Extend the built-in user model through AbstractUser:
# class CustomAccountUser(auth_models.AbstractUser):
#     age = models.PositiveIntegerField(
#         null=True,
#         blank=True,
#     )
# + in settings.py:  AUTH_USER_MODEL = "accounts.CustomAccountUser"



# 2. Extend the user model through a One-to-One relationship with a Profile model:

# 2.1 Use the built-in user model for auth:

# UserModel = get_user_model()
#
# class Profile(models.Model):
#     age = models.PositiveSmallIntegerField(
#         blank=False,
#         null=False,
#     )
#
#     user = models.OneToOneField(
#         UserModel,
#         on_delete=models.DO_NOTHING,
#         primary_key=True,
#     )  # profile_obj.pk == profile_obj.user_id



# 2.2 Create our own user model:
class AccountUserManager(auth_base.BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def with_perm(
            self, perm, is_active=True, include_superusers=True, backend=None, obj=None
                ):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


# Auth data
class CustomAccountUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        error_messages={"unique": _("A user with that email already exists."),}
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active."
            "Unselect this instead of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    # This is the other (username) part of the **credentials**
    USERNAME_FIELD = "email"

    objects = AccountUserManager()


# User data
class Profile(models.Model):
    age = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
    )

    user = models.OneToOneField(
        CustomAccountUser,
        on_delete=models.DO_NOTHING,
        primary_key=True,
        related_name="profile",
    )  # profile_obj.pk == profile_obj.user_id