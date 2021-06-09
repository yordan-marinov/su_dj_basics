from django.db import models
from django.db.models.fields import SlugField

# Create your models here.
class Post(models.Model):
    """This is a database model for blog post with fields of:
    title ------ It is characters type with max length of 240
    slug ------- It is str type and needs to be unique
    created_on - It is timestamp with creation time ordered decresingly
    content ---- It is text field to hold the content of the blog post

    Args:
        models (Model): Inherit form the Django

    Returns:
        sqlite: It returns an sqlite table
    """

    title = models.CharField(max_length=240)
    slug = models.SlugField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(
        'Author', 
        null=True, 
        on_delete=models.CASCADE
        )

    class Meta:
        # This ordering is allowing us to stack
        # latest post always to be on top
        ordering = ["-created_on"]

    def __str__(self) -> str:
        # The string preprsentation will be the post title
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.name
