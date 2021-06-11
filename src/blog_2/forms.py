from django import forms
from django.db.models import fields

from .models import Post


class PostForm(forms.Form):
    """This is Djanog form which represents the 
    Post model as a form to be filled in by customer.

    Args:
        forms (Form): Form is a method inherit from Django
    """
    
    # Title of the blog post
    title = forms.CharField(max_length=120)
    # Slug unique string indetificator
    slug = forms.SlugField()
    # Text area where the post condtend need to be filled in
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows':8, 
                'cols':25
                }
            )
        )


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = [
        #     'title',
        #     'slug',
        #     'content',
        # ]