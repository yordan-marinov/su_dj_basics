from django.db import models

# Create your models here.


class BlogPosts(models.Model):
    title = models.TextField()
    
