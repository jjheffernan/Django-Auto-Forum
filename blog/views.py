# django imports
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# local namespace imports
from blog.models import Post, Comment
from blog.forms import CommentForm


# Create your views here.
# function based index view
# need to abstract to class
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')  # by changing to class oriented, this can be separated
    # objects is a bad call
    # alternative data call
    # data = {
    #     'posts': Post.objects.all(),
    # }
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


def blog_detail(request, pk):
    # object fetch from Post model, by private key for page
    post = Post.objects.get(pk=pk)
    # alternative view method
    # post = get_object_or_404(Post, id=pk)
    # alternative data method (dict)
    # data = {
    #     'post': post,
    # }

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
