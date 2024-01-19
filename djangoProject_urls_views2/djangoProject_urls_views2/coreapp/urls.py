from django.urls import path

from djangoProject_urls_views2.coreapp.views import index_diff_params, index_json, index_render, \
    index_redirect_to_django_docs, redirect_index_render, redirect_to_index_with_params, return_error, return_exception

urlpatterns = (

    # redirects:
    path("to-django-docs/", index_redirect_to_django_docs),
    path("to-index-render/", redirect_index_render, name="redirect_to_index_render"),
    path("to-index-params/", redirect_to_index_with_params, name="redirect_to_index_params"),

    # errors:
    path("return_error/", return_error, name="error"),
    path("return_exception/", return_exception, name="exception"),

    # other:
    path("<int:pk>/", index_diff_params),
    path("<slug:slug>/", index_diff_params),
    path("<slug:slug>/<int:pk>/", index_diff_params, name="index_params"),

    path("json/<slug:slug>/<int:pk>/", index_json),

    path("", index_render),

)
