from django.db.models.fields import CharField
from django.db.models.manager import Manager
from django.urls import reverse
from django.db import models
from django.utils import timezone

# Create your models here.


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        # __lte means any post older than now
        return self.filter(publish_date__lte=now)
        # return self.get_queryset().filter(publish_date__lte=now)
        # The get_queryset()=BlogPosts.objects
        # publish_date is a field in BlogPosts model
        # __lte=less then or equal (dunder method)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class Author(models.Model):
    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BlogPosts(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(
        auto_now=False, auto_now_add=True, null=True, blank=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

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
