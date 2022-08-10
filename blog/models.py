from django.db import models

# Create your models here.


class Category(models.Model):
    """
    this is a blog Category. This file is simpler to add than a Car-specific forum
    Serves as an optional tag to place Admin Blogs for certain forums.
    The idea is to have a "sticky" space that is separate from a long thread.
    """
    name = models.CharField(max_length=32)  # added category title

    # need to add, get, post, and tag modifiers to get it to communicate with cars DB


# BLOG FORUM POST
class Post(models.Model):  # blog style post, different from project or forum post
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # categories needs to be filled out
    categories = models.ManyToManyField('Category', related_name='posts')


