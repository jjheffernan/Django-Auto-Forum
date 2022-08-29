# blog/models.py
# django imports
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    """
    this is a blog Category. This file is simpler to add than a Car-specific forum
    Serves as an optional tag to place Admin Blogs for certain forums.
    The idea is to have a "sticky" space that is separate from a long thread.
    """
    name = models.CharField(max_length=32)  # added category title

    # need to add, get, post, and tag modifiers to get it to communicate with cars DB

    def __str__(self):
        return self.name


# BLOG FORUM POST
class Post(models.Model):  # blog style post, different from project or forum post
    """
    this is the Database model for a Blog-style post on the web app.
    This is delivered differently, still uses Bootstrap like projects.
    Essentially removes comments, feedback. More optimized for keeping track of forums.
    """
    # manager class; eventually call Car project manager here
    # class ProjectManager(models.Manager):

    # Blog Post options; 'pinned', 'draft', 'published'
    blog_options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('pinned', 'Pinned'),
    )

    # Content
    title = models.CharField(max_length=255)  # same code as projects model
    body = models.TextField()  # same code as projects model, title could be build out
    status = models.CharField(max_length=10, choices=blog_options, default='draft')  # blog status

    # categories needs to be filled out
    # add accomodations for CarFields
    categories = models.ManyToManyField('Category', related_name='posts')

    # Post Metadata
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', default=None)
    # slug = models.SlugField(max_length=100, unique=True) # or unique_for_date='created_on'

    # object handling
    objects = models.Manager() # default django manager
    # car_manager = ProjectManager() # custom car manager to tag vehicles

    class Meta:
        ordering = ['-created_on']

    # def get_absolute_url(self):
    #     return reverse('post:blog_detail', args=[self.slug)  # can probably add context dict here

    def __str__(self):
        return self.title


# blog comments
class Comment(models.Model):
    author = models.CharField(max_length=60)  # length of author comment name on post
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # adds comment timestamp
    last_modified = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    # ForeignKey Defines many-to-One relationships with our Post class
    # - first arg is model for relationship.
    # - Second is to delete hanging comments on blog post on deletion

    # Comment Metadata
    class Meta:
        ordering = ['-created_on']

    # def __str__(self):
    #     return self.post
