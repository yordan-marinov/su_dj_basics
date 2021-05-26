from django import forms
from django.forms import fields

from .models import BlogPosts


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)
    
    
class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPosts
        fields = [
            'title',
            'slug',
            'content',
        ]