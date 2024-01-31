from django.shortcuts import render, redirect

from django_forms_basics.demoapp.forms import DemoClientForm, ClientForm
from django_forms_basics.demoapp.models import Client


def index(request):

    return render(request, "demoapp/index.html")


def index_basic_form(request):
    # demo_client_form = DemoClientForm(request.POST or None)

    if request.method == "GET":
        demo_client_form = DemoClientForm()

    else:  # request == "POST":
        demo_client_form = DemoClientForm(request.POST)
        if demo_client_form.is_valid():
            print(demo_client_form.cleaned_data)
            # use the data and redirect to desired page
            return redirect("index_basic_form")

    context = {"demo_client_form": demo_client_form}

    return render(request, "demoapp/index_basic_form.html", context)


def index_model_form(request):
    if request.method == "GET":
        model_form = ClientForm()

    else:
        model_form = ClientForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect("index_model_form")

    context = {
        "model_form": model_form,
        "all_clients": Client.objects.all()
    }

    return render(request, "demoapp/index_model_form.html", context)


def index_update_client(request, pk):
    client = Client.objects.get(pk=pk)

    if request.method == "GET":
        upd_form = ClientForm(instance=client)

    else:
        upd_form = ClientForm(request.POST, instance=client)
        if upd_form.is_valid():
            upd_form.save()
            return redirect("index_model_form")

    context = {
        "upd_form": upd_form,
        "client": client,
    }

    return render(request, "demoapp/index_updated_details.html", context)