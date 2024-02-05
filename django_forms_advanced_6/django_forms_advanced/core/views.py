from django.shortcuts import render, redirect

from django_forms_advanced.core.forms import UserForm, ExtendedUser
from django_forms_advanced.core.models import UserModel


def base_form(request):
    user_form = UserForm()
    readonly_form = ExtendedUser()

    context = {
        "user_form": user_form,
        "readonly_form": readonly_form,
        'all_users': UserModel.objects.all(),
    }

    return render(request, "core/index.html", context)


def create_user(request):
    # form_create = UserForm(request.POST, user=request.user)
    #
    # if form_create.is_valid():
    #     form_create.save()

    if request.method == 'POST':
        form_create = UserForm(request.POST, request.FILES, user=request.user)
        if form_create.is_valid():
            form_create.save()
            return redirect("create_user")
    else:
        form_create = UserForm(user=request.user)

    context = {
        'form_create': form_create,
    }

    return render(request, 'core/form_save.html', context)





