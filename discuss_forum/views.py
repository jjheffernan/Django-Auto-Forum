# discuss_forum/views.py

# django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# local namespace imports
from discuss_forum.models import Author, ForumCategory, ForumPost, ForumComment, Reply
from blog.models import Category
from forms import *

# Create your views here.


def forum_home(request):
    forums = Category.objects.all()
    # Maybe try get_list_or_404()
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


# detail view of forums
def forum_detail(request, slug):
    post = get_object_or_404(ForumPost, slug=slug)

    # if statements. will turn into def when swapping to CBVs
    if request.user.is_authenticated:  # checking login
        author = Author.objects.get(user=request.user)  # getting post author

    # handling comments
    if 'comment-form' in request.POST:
        comment = request.POST.get('comment')
        new_comment, created = ForumComment.objects.get_or_create(user=author, content=comment)
        post.comments.add(new_comment.id)

    # handling replies
    if 'reply-form' in request.POST:
        reply = request.POST.get('reply')
        comment_id = request.POST.get('comment-id')
        comment_obj = ForumComment.objects.get(id=comment_id)
        new_reply, created = Reply.objects.get_or_create(user=author, content=reply)

    context = {
        'post': post,
        'title': post.title,
    }
    # update_views(request, post)

    return render(request, 'detail.html', context)


def posts(request, slug):

    category = get_object_or_404(Category, slug=slug)
    posts = ForumPost.objects.filter(approved=True, categories=category)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'forum': category,
        # 'title': ,
    }

    return render(request, 'posts.html', context)


@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            print('\n\n its valid')
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()

            return redirect('home')
    context.update({
        'form': form,
        # 'title': 'Create New Post'
    })
    return render(request, 'create_post.html', context)


def latest_posts(request):
    posts = ForumPost.objects.all().filter(approved=True)[:10]
    context = {
        'posts': posts,
        # 'title': title,
    }

    return render(request, 'latest-posts.html', context)


