from django.urls import path

from CBV_basic.cbv_demo.views import MyTemplateView, TaskCreateView, TaskDetailsView

urlpatterns = (
    path("", MyTemplateView.as_view(), name="template view"),
    path("createtask/", TaskCreateView.as_view(), name="create view"),
    path("detailstask/<int:pk>/", TaskDetailsView.as_view(), name="details view"),

)