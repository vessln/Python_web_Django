from django.contrib import admin

from djangoProject_basics1.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_done']
    list_filter = ['is_done',]

# admin.site.register(Task)