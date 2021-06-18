from django import forms
from django.db.models import fields
from django.forms import widgets

from .models import Author, Post


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
        # fields = '__all__'
        exclude = ('author',)
        # fields = [
        #     'title',
        #     'slug',
        #     'content',
        # ]
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'rows': 5,
                    'cols': 65,
                }
            )
        }
        
        
class AuthorForm(forms.ModelForm):
    """Form definition for Author."""

    class Meta:
        """Meta definition for Authorform."""

        model = Author
        fields = '__all__'
