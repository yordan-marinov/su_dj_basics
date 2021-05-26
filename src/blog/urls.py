from django.urls import path

from .views import (
    blog_post_list_view,
    # blog_post_create_view,
    blog_post_retrieve_view,
    blog_post_update_view,
    blog_post_delete_view,
)


urlpatterns = [
    path("", blog_post_list_view),
    # path("create/", blog_post_create_view),
    path('<str:slug>/', blog_post_retrieve_view),
    path('<str:slug>/edit/', blog_post_update_view),
    path('<str:slug>/delete', blog_post_delete_view),
    ]
