from django.urls import path

from djangoProject_urls_views2.mainapp.views import index, index_with_params, mainapp_details_pk, mainapp_details_name


urlpatterns = (
    path("", index),
    path("prm/<param>/", index_with_params),
    path("<int:pk>/", mainapp_details_pk),
    path("<str:name>/", mainapp_details_name),

)
