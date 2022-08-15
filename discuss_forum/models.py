# discuss_forum/models.py

# django imports
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.shortcuts import reverse

# local namespace imports


# Create your models here.

User = get_user_model()


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=True)  # get nickname
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    # bio = HTMLField() # profile bio
    points = models.IntegerField(default=0) # karma/upvotes
    # profile_pic = ResizedImageField

    def __str__(self):
        return self.fullname

    @property
    def num_posts(self):
        return ForumPost.objects.filter(user=self).count()  # forum post count

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save(*args, **kwargs)


class ForumCategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    description = models.TextField(default='description')

    class Meta:  # Create metadata to interface with other categories
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(ForumCategory, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('posts', kwargs={
            'slug': self.slug,
        })

    @property
    def num_posts(self):
        return ForumPost.objects.filter(categories=self).count()

    @property
    def last_post(self):
        return ForumPost.objects.filter(categories=self).count()




