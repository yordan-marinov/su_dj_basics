from django.shortcuts import render

# Create your views here.
from .models import BlogPosts


def blog_home_page(request):
    obj = BlogPosts.objects.all()
    context = {"obj": obj}
    template_name = "blog_home_page.html"
    return render(request, template_name, context)


def blog_post_detail_page(request, pk):
    bp_obj = BlogPosts.objects.get(id=pk)
    template_name = "blog_post_detail.html"
    context = {"bp_obj": bp_obj}
    return render(request, template_name, context)
