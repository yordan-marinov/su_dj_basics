from django.db import models

# Create your models here.


class BlogPosts(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id}. {self.title}"
