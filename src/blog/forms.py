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
    
    # This validation is equal if we set unique=True in .models BlogPost.
    # The difference is that is case insensetive due to __iexact (title__iexact=title).
    def clean_title(self, *args, **kwargs):
        """This validation function is checking 
        if the title has been used in previous post,
        and if raises an ValidationError.

        Raises:
            forms.ValidationError: [It can't be used same title for different posts]

        Returns:
            [title]: [This is the form object with title equal to the given title]
        """
        # Customer's given title.
        title = self.cleaned_data.get('title') # self.cleaned_data is a dict 
        
        # Checks if the customer's title has been used.
        qs = BlogPosts.objects.filter(title__iexact=title) # title__iexact -> lookup for the same title ignoring the casing
        
        # self -> <class 'blog.forms.BlogPostModelForm'>
        instance = self.instance # self.instance -> instance is method of self (print(dir(self)))

        # print(f'===> {dir(qs)}')
        # Instance is None when we create new post 
        # Otherwise instance is not None
        if instance is not None:
            # QuerySet is equal to [] when exlude the instance we want to edit
            qs = qs.exclude(pk=instance.pk) # It could be id=instance.id, slug=instance.slug and etc.
        
        # Raises error if the customer's title exist in db else it returns it.
        if qs.exists():
            raise forms.ValidationError(
                'This title has already been used. Please enter new title!'
                )
        return title
