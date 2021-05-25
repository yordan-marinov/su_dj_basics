from django.db import models

# Create your models here.


class BlogPosts(models.Model):
    title = models.TextField()
    content = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title