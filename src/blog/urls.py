from django.urls import path

from .views import (
    blog_post_list_view,
    blog_post_create_view,
    blog_post_retrieve_view,
    blog_post_update_view,
    blog_post_delete_view,
    create_author,
)


urlpatterns = [
    path("", blog_post_list_view, name='list_name'),
    path('author/', create_author, name="create_author"),
    path("create/", blog_post_create_view, name='create_name'),
    path('<str:slug>/', blog_post_retrieve_view, name='details_name'),
    path('<str:slug>/edit/', blog_post_update_view, name='edit_name'),
    path('<str:slug>/delete', blog_post_delete_view, name='delete_name'),
    ]
