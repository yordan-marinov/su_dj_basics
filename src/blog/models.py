from django.urls import reverse
from django.db import models

# Create your models here.


class BlogPosts(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)

    # This is the string representation of the BlogPost objects (self)
    def __str__(self) -> str:
        # The objects will be representated by id. title fields of the models
        return f"{self.id}. {self.title}"

    # This way is create absloute url path which will be used in needed template
    # with this we can change url whithout the need to change it everywere just in urls.py
    def get_absolute_url(self):
        # Reverse func creates a url -> url which belong to name="details_name" / self.pk
        # Retruns /blog/slug/
        return reverse('details_name', kwargs={'slug': self.slug}) # Can be pk('pk': self.pk) or id, etc.