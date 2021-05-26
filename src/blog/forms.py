from django import forms
from django.forms import fields

from .models import BlogPosts


class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=60)
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
    
    # This validation is equal if we set unique=True in .models BlogPost
    def clean_title(self, *args, **kwargs):
        """This validation function is checking 
        if the title has been used in previous post,
        and if raises an ValidationError.

        Raises:
            forms.ValidationError: [It can't be used same title for different posts]

        Returns:
            [title]: [This is the form object with title equal to the given title]
        """
        print(self.cleaned_data)
        # Customer's given title.
        title = self.cleaned_data.get('title')
        
        # Checks if the customer's title has been used.
        qs = BlogPosts.objects.filter(title=title)
        
        # Raises error if the customer's title exist in db else it returns it.
        if qs.exists():
            raise forms.ValidationError(
                'This title has already been used. Please enter new title!'
                )
        return title
