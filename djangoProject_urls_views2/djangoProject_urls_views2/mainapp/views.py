from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("First view!")


def index_with_params(request, *args, **kwargs):
    return HttpResponse(f"Args: {args}. Kwargs: {kwargs}")


def mainapp_details_pk(request, pk):
    return HttpResponse(F"Return parameter pk: {pk}")


def mainapp_details_name(request, name):
    return HttpResponse(F"Return parameter name: {name}")








