from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm


def todo_list(request):
    qs = Task.objects.all()

    template_name = "todo/todo_list.html"
    context = {"tasks": qs}
    return render(request, template_name, context)


def todo_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("todo_list")

    template_name = "todo/todo_create.html"
    context = {"form": form}
    return render(request, template_name, context)


def todo_edit(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("todo_list")

    context = {"form": form}
    return render(request, "todo/todo_edit.html", context)
