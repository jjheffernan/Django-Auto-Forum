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
