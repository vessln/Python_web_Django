from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("CBV_basic.core.urls")),
    path("cbv/", include("CBV_basic.cbv_demo.urls")),

]
