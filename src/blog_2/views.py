from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Post
from .forms import PostForm, PostModelForm

# CRUD
# 1. List
# 2. Create
# 3. Details
# 4. Update -> url: Edit
# 5. Delete


def list_page(request):
    """This is a view function wich takes request object
    and render html file dynamicaly by giving db objects.
    It list out all blog posts.

    Args:
        request : Client request object passed by django

    Returns:
        html: Dynamicly generated view of the html template
    """
    qs = Post.objects.all()
    template_name = "blog_2/list.html"
    context = {"page_name": "list_page", "obj": qs}
    return render(request, template_name, context)

    # This Create Page View is using the form.Form
    # def create_page(request):
    form = PostForm(request.POST or None)
    if form.is_valid():

        # This is simple print debug
        # Only to get my head around of form instance
        # And there is no need to do it at all
        print("===> It works!")
        print(f"===> {form.__dict__}")
        print(f"===> Form: {form.cleaned_data}")

        # Creating a Model instance by create method of the Post object
        # And passing kwargs of the form.cleaned_data
        Post.objects.create(**form.cleaned_data)

        # Redirect to the empty post form after creating Post instance
        return HttpResponseRedirect("/blog-2-new")

    template_name = "blog_2/create.html"
    context = {"form": form}
    return render(request, template_name, context)

    # def create_page(request):
    pass


# This Create Page View is using the form.ModelForm
def create_page(request):
    """This is a func which renders ModelForm 
    which needs to be filled in correctly by the user
    and returns respose.

    Args:
        request : Client request to create a new post

    Returns:
        Render http response with the valid filled form
    """
    # assign postmodelform instance to the form var
    form = PostModelForm(request.POST or None)

    # Checks if the form is with valid input
    if form.is_valid():
        # Seves the data from the form to the Post model(db)
        form.save()
        # It redirects customer to the blog-2 list view
        return HttpResponseRedirect("/blog-2")

    template_name = "blog_2/create.html"
    context = {"form": form}

    return render(request, template_name, context)


def details_page(request, slug):
    """This funcition render detail view of the each post
    by showing the post title, date on which is been created
    and also the content.

    Args:
        request : Client request passed by django
        slug (str): Unique string identification

    Returns:
        html: Dynamicly generated view of the html template
    """

    # It returns Post object if slug is valid
    # otherwise raise 404 error exeption
    qs = get_object_or_404(Post, slug=slug)
    template_name = "blog_2/detais.html"
    context = {"post_obj": qs}

    return render(request, template_name, context)


def update_page(request, slug):
    qs = get_object_or_404(Post, slug=slug)
    form = PostModelForm(request.POST or None, instance=qs)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/blog-2")

    template_name = "blog_2/create.html"
    context = {"form": form}

    return render(request, template_name, context)


def delete_page(request, slug):
    """It Delete the object with the given slug 
    if is not found raise 404 exeption
    and returns redirected responce to the blog_2 list.

    Args:
        request: Customers request pass by Django
        slug (str): Unique str identification field set by the author of the post

    Returns:
        Http: Redirected to the blog_2 list
    """
    
    qs = get_object_or_404(Post, slug=slug)
    qs.delete()
    return HttpResponseRedirect("/blog-2")
