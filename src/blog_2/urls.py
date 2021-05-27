from django.urls import path

from .views import(
    list_page,
    create_page,
    details_page,
    update_page,
    delet_page,
)

urlpatterns = [
    path("", list_page, name='list'),
    ]