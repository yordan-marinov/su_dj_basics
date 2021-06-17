from django.shortcuts import redirect, render, get_object_or_404

from .models import Post
from .forms import PostForm, PostModelForm

# CRUD
# 1. List
# 2. Create
# 3. Details
# 4. Update -> url: Edit
# 5. Delete


def list_page(request):
    qs = Post.objects.all()
    template_name = "blog_2/list.html"
    context = {"page_name": "Posts", "posts": qs}

    return render(request, template_name, context)

    # ===  Create Page View is using the form.Form ==========================
    form = PostForm(request.POST or None)
    if form.is_valid():
        # print("===> It works!")
        # print(f"===> {form.__dict__}")
        # print(f"===> Form: {form.cleaned_data}")
        # Creating a Model instance by create method of the Post object
        # And passing kwargs of the form.cleaned_data
        Post.objects.create(**form.cleaned_data)
        # Redirect to the empty post form after creating Post instance
        return redirect("create")
    template_name = "blog_2/create.html"
    context = {"form": form}
    return render(request, template_name, context)
    # ======================================================================


def create_page(request):
    form = PostModelForm(request.POST or None)

    # Checks if the form is with valid input
    if form.is_valid():
        # Seves the data from the form to the Post model(db)
        form.save()
        # It redirects customer to the blog-2 list view
        return redirect("list")

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
    obj = get_object_or_404(Post, slug=slug)
    template_name = "blog_2/detais.html"
    context = {"page_name": "Details", "post_obj": obj}

    return render(request, template_name, context)


def update_page(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    form = PostModelForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("list")

    template_name = "blog_2/create.html"
    context = {"page_name": "Updates", "form": form}

    return render(request, template_name, context)


def delete_page(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect("list")

    context = {"page_name": "Delete", "post": obj}
    return render(request, "blog_2/delete.html", context)
