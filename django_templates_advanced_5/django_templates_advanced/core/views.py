from django.shortcuts import render

toys = {
    "ball": 3,
    "wool": 1,
    "mouse": 7,
    "fish": 1
}


def index(request):
    context = {}

    return render(request, "base.html")


def about(request):
    context = {}

    return render(request, "core/about.html")


def stuffs(request):
    context = {
        "toys": toys,
    }

    return render(request, "core/stuffs.html", context)
