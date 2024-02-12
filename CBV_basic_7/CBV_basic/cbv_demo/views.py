from datetime import datetime

from django.forms import DateInput
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from CBV_basic.cbv_demo.forms import TaskForm
from CBV_basic.cbv_demo.models import TaskModel


class MyTemplateView(views.TemplateView):
    # static templates:
    template_name = "cbv_demo/cbv_template.html"

    # dynamic templates:
    # def get_template_names(self):


    # static context - no database calls:
    extra_context = {
        "static_data": "Context with static data.",
    }

    # dynamic context - database calls etc:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["dynamic_data"] = datetime.now()

        context["all_tasks"] = TaskModel.objects.all()

        return context


class TaskCreateView(views.CreateView):
    # create form with modelform_factory:
    model = TaskModel
    fields = "__all__"
    template_name = "cbv_demo/cbv_create.html"


    # static way to redirect:
    success_url = reverse_lazy("template view")

    #dynamic way to redirect:
    def get_success_url(self):
        return reverse("details view", kwargs={"pk": self.object.pk})


    # static way to create form:
    # form_class = TaskForm

    # dynamic way to create form:
    def get_form_class(self):
        # logic for returning other form, not default:
        # return TaskForm

        return super().get_form_class()

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        # form.fields["deadline"].widget.attrs["type"] = "date"

        deadline_field_data = {
            "type": "date",
            "dateFormat": "d-M-y",
            "placeholder": "d-M-y",
            "class": "datefield",
        }

        form.fields["deadline"].widget = DateInput(deadline_field_data)

        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["all_tasks"] = TaskModel.objects.all()

        return context

    def form_valid(self, form):
        # my custom validation (clean) -> if i make custom validations it is better to make individual form
        return super().form_valid(form)


class TaskDetailsView(views.DetailView):
    model = TaskModel
    template_name = "cbv_demo/cbv_details.html"
