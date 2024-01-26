from django.urls import path

from django_forms_basics.demoapp.views import index, index_basic_form, index_model_form, index_update_client

urlpatterns = (
    path("", index, name="index"),
    path("form/", index_basic_form, name="index_basic_form"),
    path("modelform/", index_model_form, name="index_model_form"),
    path("modelform/<int:pk>/", index_update_client, name="index_update_client")

)