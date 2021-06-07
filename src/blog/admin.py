from django.contrib import admin

# Register your models here.
from .models import BlogPosts, Author


admin.site.register(BlogPosts)
admin.site.register(Author)
