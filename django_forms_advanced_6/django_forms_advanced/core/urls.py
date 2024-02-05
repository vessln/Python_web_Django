from django.urls import path

from django_forms_advanced.core.views import base_form, create_user

urlpatterns = (
    path("", base_form, name="base_form"),
    path("create_user/", create_user, name="create_user")
)