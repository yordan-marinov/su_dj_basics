from django.urls import path

from .views import blog_home_page, blog_all_posts_page


urlpatterns = [
    path('', blog_home_page), 
    path('<int:pk>/', blog_all_posts_page),
]