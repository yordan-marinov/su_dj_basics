from django.shortcuts import render

from .models import Post

# CRUD
# 1. List
# 2. Create
# 3. Details
# 4. Update -> url: Edit
# 5. Delete

def list_page(request):
    """This is a view function wich takes request object
    and render html file dynamicaly by giving db objects

    Args:
        request : Client request object passed by django

    Returns:
        html: Dynamicly generated view of the html template
    """
    p = Post.objects.all()
    template_name = 'blog_2/list.html'
    context = {'page_name': "list_page", "obj": p}
    return render(request, template_name, context)


def create_page(request):
    pass

def details_page(request):
    pass

def update_page(reqeust):
    pass

def delet_page(request):
    pass

