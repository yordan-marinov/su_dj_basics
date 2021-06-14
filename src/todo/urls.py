from django.urls import path

from .views import todo_create, todo_edit, todo_list

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('create/', todo_create, name='todo_create'),
    path('edit/<int:pk>', todo_edit, name='todo_edit'),
]