from django.urls import path

from .views import(
    list_page,
    details_page,
    update_page,
    delete_page,
)

urlpatterns = [
    path("", list_page, name='list'),
    path('<str:slug>/', details_page, name='details'),
    path('<str:slug>/edit/', update_page, name="update"),
    path('<str:slug>/delete/', delete_page, name='delete'),
    ]