from django.urls import path

from django_templates_advanced.core.views import index, about, stuffs

urlpatterns = (
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("stuffs/", stuffs, name="stuffs"),

)