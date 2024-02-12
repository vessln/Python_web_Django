from django import forms

from CBV_basic.cbv_demo.models import TaskModel


class TaskForm(forms.Form):
    class Meta:
        model = TaskModel
        fields = "__all__"
