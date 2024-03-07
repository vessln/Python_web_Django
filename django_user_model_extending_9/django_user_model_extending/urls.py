from django.contrib import admin
from django.urls import path, include

from django_user_model_extending.accounts.views import LoginUserView, RegisterUserView, LogoutUserView
from django_user_model_extending.common.views import home_page, AboutView


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home_page, name="home page"),
    # path("about/", about_page, name="about"),
    path("about/", AboutView.as_view(), name="about"),
    path("accounts/login/", LoginUserView.as_view(), name="login user"),
    path("accounts/register/", RegisterUserView.as_view(), name="register user"),

    path("logout/", LogoutUserView.as_view(), name="logout user"),

]
