from django.contrib import admin

# Register your models here.
from .models import Post


# Registering the Post model into our admin panel
admin.site.register(Post)
