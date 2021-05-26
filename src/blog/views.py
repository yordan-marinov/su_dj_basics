from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPosts


def blog_home_page(request):
    obj = BlogPosts.objects.all()
    context = {"obj": obj}
    template_name = "blog_home_page.html"
    return render(request, template_name, context)


def blog_all_posts_page(request, slug):
    bp_obj = get_object_or_404(BlogPosts, slug=slug)
    template_name = "blog_all_posts.html"
    context = {"bp_obj": bp_obj}
    return render(request, template_name, context)


# CRUD -> Create Retrieve(Detail) Update Delete

# GET -> Retrieve(Detail): 1 object / List: several objects

# Post -> Create / Update / DELETE


def blog_post_list_view(request):
    """List out objects also could be search as well"""

    template_name = "blog_post_list.html"
    context = {"obj_list": []}
    return render(request, template_name, context)


def blog_post_create_view(request):
    """Create objects of the given model and use a form"""

    template_name = "blog_post_create.html"
    context = {"form": None}
    return render(request, template_name, context)


def blog_post_retrieve_view(request, slug):
    """It render one object or the details of the given object view"""

    bp_obj = get_object_or_404(BlogPosts, slug=slug)
    template_name = "blog_post_retrive.html"
    context = {"bp_obj": bp_obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    """It update the given object and is using a form"""

    bp_obj = get_object_or_404(BlogPosts, slug=slug)
    template_name = "blog_post_update.html"
    context = {"bp_obj": bp_obj, "form": None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    """It delete the given object"""

    bp_obj = get_object_or_404(BlogPosts, slug=slug)
    template_name = "blog_post_delete.html"
    context = {"bp_obj": bp_obj}
    return render(request, template_name, context)
