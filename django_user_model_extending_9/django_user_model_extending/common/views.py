from django import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render


def home_page(request):

    return render(request, "common/home-page.html")


# @login_required
# def about_page(request):
#
#     return render(request, "common/about-page.html")

# or:

class AboutView(auth_mixins.LoginRequiredMixin, views.View):
    def get(self, request):
        return render(request, "common/about-page.html")
