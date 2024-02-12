from django import views
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView


def function_based_view(request):
    if request.method == "POST":
        pass  # logic for post method
    else:
        pass  # logic for get method

    context = {}

    return render(request, "core/index.html", context)


class CBView(views.View):
    def dispatch(self, request, *args, **kwargs):  # execute some logic before current view
        # if not user.is_authenticated:
        #     raise HttpResponseNotAllowed(["get"])

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "core/index.html")

    def post(self, request):
        pass  # logic for post method


class BaseView:  # Parent of class based views (like View)
    @classmethod
    def as_view(cls):
        def view(request, *args, **kwargs):
            """
            make an instance of the class through which the method
            `as_view` is called (as_view.MyClassView -> MyClassView):
            """
            self = cls()
            if request.method == "POST":
                return self.post(request, *args, **kwargs)
            else:
                return self.get(request, *args, **kwargs)

        return view


class MyClassView(BaseView):
    def get(self, request):
        return HttpResponse("Response from class based view `MyView`.")


def indexview(request):
    return HttpResponse("Response from function based view `indexview`.")









