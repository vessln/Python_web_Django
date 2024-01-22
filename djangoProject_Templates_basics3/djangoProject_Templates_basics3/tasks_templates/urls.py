from django.urls import path

from djangoProject_Templates_basics3.tasks_templates.views import index, menu_index

urlpatterns = (
    path("", index, name="index"),
    path("menu/<option>", menu_index, name="menu"),

)
