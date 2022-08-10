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
    """
    this is the Database model for a Blog-style post on the web app.
    This is delivered differently, still uses Bootstrap like projects.
    Essentially removes comments, feedback. More optimized for keeping track of forums.
    """
    title = models.CharField(max_length=255)  # same code as projects model
    body = models.TextField()  # same code as projects model, title could be build out
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # categories needs to be filled out
    # add accomodations for CarFields
    categories = models.ManyToManyField('Category', related_name='posts')


# blog comments
class Comment(models.Model):
    author = models.CharField(max_length=60)  # length of author comment name on post
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # adds comment timestamp
    # comments cannot be edited at this time
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    # ForeignKey Defines many-to-One relationships with our Post class
    # - first arg is model for relationship.
    # - Second is to delete hanging comments on blog post on deletion

