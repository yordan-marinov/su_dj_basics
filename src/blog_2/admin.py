from django.contrib import admin

# Register your models here.
from .models import (
    Post,
    Author,
)


# Registering the Post model into our admin panel
# admin.site.register(Post)


class InLineAuthor(admin.StackedInline):
    # By this we are adding a Post form into the Author page in admin
    model = Post
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Displays the given fields as columns
    list_display = (
        "title",
        "slug",
        "created_on",
    )
    # Create the link with the given field
    list_display_links = ("title",)
    # The field can be edit wihout to go to the edit page
    list_editable = ("slug",)
    # To be able to search post with the given fields
    list_filter = (
        "title",
        "slug",
        "created_on",
    )
    # Search bar with the given fields to be searched in
    search_fields = ("title", "slug", "created_on")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # This are the all inlines we want to add to the admin page
    inlines = [InLineAuthor]
    
    list_display = ("name", "email")
    list_display_links = ("name",)
