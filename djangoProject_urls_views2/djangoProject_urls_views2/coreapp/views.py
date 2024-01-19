from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index_diff_params(request, *args, **kwargs):
    context = (f"Try many parameters: args - {args},"
               f" kwargs - {kwargs},"
               f" path: {request.path}")

    return HttpResponse(context)

# http://127.0.0.1:8000/coreapp/vesi/25/
# Try many parameters: args - (), kwargs - {'slug': 'vesi', 'pk': 25} on path: /coreapp/vesi/25/


def index_json(request, *args, **kwargs):
    context = {"args": args,
               "kwargs": kwargs,
               "path": request.path,
               }

    return JsonResponse(
        context,
        # content_type="application/json"
    )


def index_render(request):
    context = {
        "title": "Coreapp template",
        "method": request.method,
    }

    return render(request, "coreapp/index.html", context)


def index_redirect_to_django_docs(request):
    return redirect("https://docs.djangoproject.com")


def redirect_index_render(request):
    return redirect("redirect_to_index_render")


def redirect_to_index_with_params(request):
    return redirect("index_params", slug="veselina", pk=1998)


def return_error(request):
    return HttpResponseNotFound(
        status=404,
    )


def return_exception(request):
    raise Http404


