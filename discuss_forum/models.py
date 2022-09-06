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
    points = models.IntegerField(default=0)  # karma/upvotes
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


# may also be referred to as topics, this is the basis of the forums. Tags aside
class ForumCategory(models.Model):
    """Categories Serve the front end of the website. The basis of how the forum table is viewed."""
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


# child of Forum Category
class SubForum(models.Model):
    pass


# -- Forum Post Interaction --
# reddit style replies to original comments
class Reply(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment_content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content[:100]

    class Meta:
        verbose_name_plural = 'replies'


# Forum Comment on Post
class ForumComment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment_content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    replies = models.ManyToManyField(Reply, blank=True)

    def __str__(self):
        return self.comment_content[:100]


# Posts to Sub-forum
class ForumPost(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    # content = HTMLField() #tinymce field
    content = models.TextField()

    # categories
    categories = models.ManyToManyField(ForumCategory)
    create_date = models.DateTimeField(auto_now_add=True)

    # hit count amount
    # generic_hit_count = GenericRelation(HitCount)

    # tags
    # tags = TaggableManager()

    # comments
    comments = models.ManyToManyField(ForumComment, blank=True)

    # post booleans
    approved_post = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    post_state = models.CharField(max_length=40, default='zero')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(ForumPost, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('detail',
                       kwargs={
                           'slug': self.slug,
                       })

    # -- for forum homepage views --
    # @property
    # def num_comments(self):
    #     # number of comments
    #     return self.comments.count()
    #
    # @property
    # def last_reply(self):
    #    # latest reply for view
    #     return self.comments.latest('date')


