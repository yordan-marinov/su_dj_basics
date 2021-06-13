from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'task',
        'complete',
        'created_on',
        'priority',
        )
    list_editable = ('priority',)