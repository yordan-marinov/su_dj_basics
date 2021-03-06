from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponseRedirect
from .forms import AuthorForm, BlogPostModelForm
from .models import BlogPosts

# CRUD -> Create Retrieve(Detail) Update Delete

# GET -> Retrieve(Detail): 1 object / List: several objects

# Post -> Create / Update / DELETE


def blog_post_list_view(request):
    """List out objects also could be search as well"""

    #qs = BlogPosts.objects.filter(title_contains='whatever')
    # If we filter, that way is how we can use it as search.
    qs = BlogPosts.objects.published()
    # published() is from the BlogPostManager objects manager passed to the model
    
    template_name = "blog/list.html"
    context = {"obj_list": qs}
    
    return render(request, template_name, context)


def blog_post_create_view(request):
    """Create objects of the given model and use a form"""
    
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        # bp_obj = BlogPosts.objects.create(**form.cleaned_data)
        form.save()
        return redirect("list_name")

    template_name = "blog/create.html"
    context = {"form": form}
    return render(request, template_name, context)


def create_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('create_name')

    context = {'form': form}
    return render(request, 'blog/create_author.html', context)


def blog_post_retrieve_view(request, slug):
    """It render one object or the details of the given object view"""

    bp_obj = get_object_or_404(BlogPosts, slug=slug)
    template_name = "blog/retrive.html"
    context = {"bp_obj": bp_obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    """It update the given object and is using a form"""

    qs = get_object_or_404(BlogPosts, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=qs)
    
    if form.is_valid():
        form.save()
        form = BlogPostModelForm()
    
    template_name = "form.html"
    context = {"bp_obj": qs, "form": form}
    
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    """It delete the given object"""

    qs = get_object_or_404(BlogPosts, slug=slug)
    if request.method == 'POST':
        qs.delete()
        return redirect('/blog')

    template_name = "blog/delete.html"
    context = {"object": qs}
    return render(request, template_name, context)
