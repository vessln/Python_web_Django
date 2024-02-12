from django.urls import path

from CBV_basic.core.views import function_based_view, indexview, MyClassView

urlpatterns = (
    path("", function_based_view, name="function based view"),

    path("indexview/", indexview, name="index view"),
    path("myclassview/", MyClassView.as_view(), name="my class view"),

)