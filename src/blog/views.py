from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPosts


def blog_home_page(request):
    obj = BlogPosts.objects.all()
    context = {"obj": obj}
    template_name = "blog_home_page.html"
    return render(request, template_name, context)


def blog_all_posts_page(request, pk):
    bp_obj = get_object_or_404(BlogPosts, id=pk)
    template_name = "blog_all_posts.html"
    context = {"bp_obj": bp_obj}
    return render(request, template_name, context)
