# django imports
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# local namespace imports
from blog.models import Post, Comment
from .forms import CommentForm


# Create your views here.
class BlogIndexView(ListView):

    # declare variables here
    model = Post
    template_name = "blog_index.html"
    context_object_name = 'posts'

    # def __str__(self):
        # this is part of the initialization of a view

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on') # by changing to class oriented, this can be separated
    # objects is a bad call
    context = {
        'posts': posts,
    }
    return render(request, 'blog_index.html', context)


def blog_category(request, category):
    # pull from db
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')
    # define context
    context = {
        'category': category,
        'posts': posts
    }
    # return rendered html template
    return render(request, 'blog_category.html', context)


# blog detail view
class BlogDetailView(DetailView):

    model = Post
    template_name = "blog_detail.html"
    context_object_name = "posts"


def blog_detail(request, pk):
    # object fetch from Post model, by private key for page
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )

    # filter comments by post
    comments = Comment.objects.filter(post=post)
    # define context
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    # return rendered html template.
    return render(request, 'blog_detail.html', context)
