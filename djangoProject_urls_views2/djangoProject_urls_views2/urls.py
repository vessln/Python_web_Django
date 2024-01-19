"""
URL configuration for djangoProject_urls_views2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from djangoProject_urls_views2.mainapp.views import index, index_with_params, mainapp_details_pk, mainapp_details_name

urlpatterns = [
    path("admin/", admin.site.urls),

    path("coreapp/", include("djangoProject_urls_views2.coreapp.urls")),

    # prefix with "mainapp" all urls defined in djangoProject_urls_views2.mainapp.urls
    path("mainapp/", include("djangoProject_urls_views2.mainapp.urls")),

    # path("mainapp/", include([
    #     path("", index),
    #     path("prm/<param>/", index_with_params),
    #     path("<int:pk>/", mainapp_details_pk),
    #     path("<str:name>/", mainapp_details_name),
    # ])),

]
