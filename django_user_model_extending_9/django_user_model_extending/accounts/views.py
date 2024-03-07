from django.views import generic as views
from django.contrib.auth import views as auth_views, authenticate, login, get_user_model
from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy, reverse

from django_user_model_extending.accounts.forms import CustomUserCreationForm

#  authenticate(request ,**credentials) -> if credentials match returns User
#  login(request, user) -> attaches a cookie for the authenticated user for current session


# correct way to get the User model
UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    # form_class = auth_forms.UserCreationForm  # built-in form
    form_class = CustomUserCreationForm    # my custom form
    template_name = "accounts/register_user.html"
    success_url = reverse_lazy("home page")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)  # log the user in after registration
        return response


class LoginUserView(auth_views.LoginView):
    template_name = "accounts/login_user.html"

    # def get_success_url(self):
    #     return reverse("home page")


class LogoutUserView(auth_views.LogoutView):
    template_name = "common/home-page.html"

    def get_success_url(self):
        return reverse("home page")  # not work ?!



# class LoginView(auth_views.LoginView):
#     forms_class = auth_forms.AuthenticationForm
#
#     # template_name = "accounts/login_user.html"
#     # success_url = reverse_lazy("home_page")
#
#     def get(self, request, *args, **kwargs):
#         context = {
#             "form": self.forms_class(),
#         }
#
#         return render(request, "accounts/login_user.html", context)
#
#     def post(self, request, *args, **kwargs):
#         username, password = request.POST["username"], request.POST["password"]
#         user = authenticate(username=username, password=password)
#
#         if user is not None:
#             # add the user to the current session
#             login(request, user)
