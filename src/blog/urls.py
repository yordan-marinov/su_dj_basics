from django.urls import path

from .views import blog_home_page, blog_post_detail_page


urlpatterns = [
    path('', blog_home_page), 
    path('<int:pk>/', blog_post_detail_page),
]