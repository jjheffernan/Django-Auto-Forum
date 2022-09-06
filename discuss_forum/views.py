# discuss_forum/views.py

# django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView, TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# local namespace imports
from discuss_forum.models import *
from blog.models import Category
from discuss_forum.forms import *


# Create your views here.
# forum home view (class based)
class ForumHome(ListView):
    model = ForumPost
    template_name = 'forum_index.html'
    context_object_name = 'forum_posts'
    # queryset = ForumPost.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # calls base implementation
        # add queryset
        context['forum_list'] = ForumPost.objects.all()
        return context


# list view of forum topics
class ForumCatIndexView(ListView):
    model = ForumCategory
    template_name = 'forum_topic_index.html'
    context_object_name = 'category'

    class Meta:
        # context
        ordering = []
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # calls base implementation
        # add queryset
        context['forum_list'] = ForumPost.objects.all()
        return context


# class based view of specific Forum/Subforum view
class ForumPostIndexView(ListView):
    template_name = 'forum_index.html'
    model = ForumPost
    context_object_name = 'post'
    post = get_object_or_404(ForumPost)  # might need to add slug here or filter by slug


class ForumPostDetailView(DetailView):
    template_name = 'forum_detail.html'
    model = ForumPost
    context_object_name = 'post'
    post = get_object_or_404(ForumPost)

    class Meta:
        pass


@login_required
class CreateForumCategory(CreateView):
    model = ForumCategory
    template_name = 'create_forum_topic'
    context_object_name = 'category'

    class Meta:
        # context
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # calls base implementation
        # add queryset
        context['forum_list'] = ForumPost.objects.all()
        return context


@login_required
class CreateSubForum(CreateView):
    model = SubForum
    template_name = 'create_subforum'
    context_object_name = 'subforum'
    # requires admin permission

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # calls base implementation
        # add queryset
        context['forum_list'] = ForumPost.objects.all()
        return context


@login_required
class CreateForumPost(CreateView):
    model = ForumPost
    template_name = 'create_forum_post'
    context_object_name = 'post'
    forms = ('comment_form', 'reply_form')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # calls base implementation
        # add queryset
        context['forum_list'] = ForumPost.objects.all()
        return context

    # this isn't functional implementation, just a code reminder to make forms
    def comment_form(self, request):
        pass

    def reply_form(self, request):
        pass


# - function based views (legacy) -
# forum home page view, does not show posts or topics
def forum_home(request):
    forums = Category.objects.all()
    # Maybe try get_list_or_404()
    # num_posts = ForumPost.objects.all.count()
    # num_users = User.objects.all.count()
    # num_categories = forums.count()

    # bad implementation
    try:
        last_post = ForumPost.objects.latest('date')
    except:
        last_post = []

    context = {
        'forums': forums,
        # 'num_posts': num_posts,
        # 'num_users': num_users,
        # 'num_categories': num_categories,
        'last_post': last_post,
        # 'title': 'forum title',
    }

    return render(request, 'forum_home.html', context)


# forum posts index view, migrated from blog
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


# detail view of forums
def forum_post_detail(request, slug):
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


