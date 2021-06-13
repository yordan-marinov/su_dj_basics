from django.shortcuts import render
from django.http import HttpResponse

from .models import Task


def todo_list(request):
    qs = Task.objects.all()
    template_name = 'todo/list.html'
    context = {"tasks": qs}
    return render(request, template_name, context)