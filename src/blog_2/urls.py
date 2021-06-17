from django.urls import path

from .views import(
    list_page,
    create_page,
    details_page,
    update_page,
    delete_page,
)

urlpatterns = [
    path("", list_page, name='list'),
    path("create/", create_page, name="create"),
    path('<str:slug>/', details_page, name='details'),
    path('<str:slug>/update/', update_page, name="update"),
    path('<str:slug>/delete/', delete_page, name='delete'),
    ]