"""django101 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include

# Custom imports
from .views import home_page, about_page, contact_page
from blog.views import blog_post_create_view
from blog_2.views import create_page
from todo.views import todo_create


urlpatterns = [
    # This are the urls of the first blog
    path("blog-new/", blog_post_create_view),
    path("blog/", include("blog.urls")),

    # This are the urls of the second blog
    path("blog-2/", include("blog_2.urls")),
    path("blog-2-new/", create_page, name="create"),

    # This are the urls of the todo app
    path("todo/", include("todo.urls")),

    # This are the urls of the main app urls
    path("", home_page),
    path("about/", about_page),
    path("contact/", contact_page),

    # Built in admin url
    path("admin/", admin.site.urls),
]
