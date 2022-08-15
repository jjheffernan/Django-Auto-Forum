# discuss_forum/views.py

# django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# local namespace imports
from discuss_forum.models import Author, ForumCategory, ForumPost, ForumComment, Reply
from blog.models import Category

# Create your views here.


def forum_home(request):
    forums = Category.objects.all()
    num_posts = ForumPost.objects.all.count()
    num_users = User.objects.all.count()
    num_categories = forums.count()

    # bad implementation
    try:
        last_post = ForumPost.objects.latest('date')
    except:
        last_post = []

    context = {
        'forums': forums,
        'num_posts': num_posts,
        'num_users': num_users,
        'num_categories': num_categories,
        'last_post': last_post,
        # 'title': 'forum title',
    }

    return render(request, 'forum_home.html', context)


