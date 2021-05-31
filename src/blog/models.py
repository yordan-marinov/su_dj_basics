from django.urls import reverse
from django.db import models
from django.utils import timezone

# Create your models here.


class BlogPostManager(models.Manager):
    def published(self):
        now = timezone.now()
        
        # __lte means any post older than now 
        return self.get_queryset().filter(published_date__lte=now)
        # The get_queryset()=BlogPosts.objects
        # __lte=less then or equal (dunder method)

class BlogPosts(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = BlogPostManager()

    class Meta:
        ordering = ["-publish_date", "-updated", "-timestamp"]

    # This is the string representation of the BlogPost objects (self)
    def __str__(self) -> str:
        # The objects will be representated by id. title fields of the models
        return f"{self.id}. {self.title}"

    # This way is create absloute url path which will be used in needed template
    # with this we can change url whithout the need to change it everywere just in urls.py
    def get_absolute_url(self):
        # Reverse func creates a url -> url which belong to name="details_name" / self.pk
        # Retruns /blog/slug/
        return reverse(
            "details_name", kwargs={"slug": self.slug}
        )  # Can be pk('pk': self.pk) or id, etc.
