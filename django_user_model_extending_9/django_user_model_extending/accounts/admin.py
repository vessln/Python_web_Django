from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth import admin as auth_admin

from django_user_model_extending.accounts.forms import CustomUserCreationForm, AccountUserChangeForm

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(auth_admin.UserAdmin):
    list_display = ("email", "is_staff", "is_superuser",)
    ordering = ("email", )

    form = AccountUserChangeForm
    add_form = CustomUserCreationForm


