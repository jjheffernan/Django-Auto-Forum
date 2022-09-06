# blog/views.py

# django imports
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# local namespace imports
from blog.models import BlogPost, Comment
from blog.forms import CommentForm


# Create your views here.

# Index View
class BlogIndexView(ListView):

    # declare variables here
    model = BlogPost
    template_name = "blog_index.html"
    context_object_name = 'posts'
    # context_object_name = 'blog_list'  # alternative object in ORM
    # paginate_by = 5
    # ordering = [-date_posted']

    # def __str__(self):
    #     # this is part of the initialization of a view
    #     return self.template_name

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['posts'] = BlogPost.objects.all()
    #     return context


# Category View
class BlogCategoryView(ListView):
    model = BlogPost
    template_name = 'blog_category.html'
    context_object_name = 'posts'
    # context_object_name = 'blog_cat_list'  # alternative object in ORM
    # paginate_by = 2

    # method override does not work, needs to return category as title
    # def get_queryset(self):
    #     content = {
    #         'cat': self.kwargs['category'],
    #         'posts': BlogPost.objects.filter(category__name=self.kwargs['category']).filter(status='published')
    #     }
    #     return BlogPost.objects.filter(blog_category__icontains=self.kwargs.get('categories'))
    #     return content
    # when not overwritten, site displays but without header

    # may need to add get_context_data
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['category'] = get_object_or_404(BlogPost, category=self.kwargs.get('category'))
    #     context['posts'] = get_object_or_404(BlogPost, pk=self.kwargs.get('pk'))


class BlogUserPostView(ListView):
    model = BlogPost
    template_name = 'user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return BlogPost.objects.filter(author=user).order_by('-date_posted')


# blog detail view
class BlogDetailView(DetailView):

    model = BlogPost
    template_name = "blog_detail.html"
    form = CommentForm()
    # comments = Comment.objects.filter(post=)
    context_object_name = 'post'
    # pk_url_kwarg = 'custom_pk'

    def __str__(self):
        return BlogPost.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['posts'] = BlogPost.objects.filter(id=self.kwargs.get('id'))
        # context['posts'] = get_object_or_404(BlogPost, pk=self.kwargs.get('pk'))
        context['posts'] = get_object_or_404(BlogPost, pk=self.kwargs.get('pk'))
        # context['comments'] = Comment.objects.filter(id=self.kwargs.get('pk'))
        return context

    def post(self, request, pk):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = Comment(
                    author=form.cleaned_data['author'],
                    body=form.cleaned_data['body'],
                    post=BlogPost
                )
        # return comment
        return HttpResponse


# CRUD method classes for Blog Posts
# Create New Blog Post
# test_func is for UserPassesTestMixin, but is redundant since element is not shown. Security rework here later
class AddBlog(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = BlogPost
    template_name = 'create_blog.html'
    fields = '__all__'
    # success_url = reverse_lazy('blog/index')  # fixed syntax. correct redirect to new post url

    # def get_success_url(self):
    #     messages.success(
    #         self.request, 'Your Post has been Created'
    #     )
    #     return reverse_lazy('blog/index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        blog_object = form.save(commit=False)
        blog_object.author = self.request.user
        # obj.slug = slugify(form.cleaned_data['title'])
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     return context

    def test_func(self):
        # user = authenticate(username=self.request.user.username)
        user = self.request.user.is_authenticated
        if user is not False:  # FIX THIS IMPLEMENTATION GOOFBALL
            return True
            # A backend authenticated the credentials
        return False
        # add redirect to login here
        # No backend authenticated the credentials


# Edit Existing Blog Post
class EditBlog(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    template_name = 'edit_blog.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blog:posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object(BlogPost)
        if self.request.user == post.author:
            return True
        return False


# Delete Existing Blog Post
class DeleteBlog(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'confirm_delete_blog.html'
    # pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blog:posts')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# legacy function based views

# def blog_index(request):
#     posts = BlogPost.objects.all().order_by('-created_on')  # by changing to class oriented, this can be separated
#     # objects is a bad call
#     # alternative data call
#     # data = {
#     #     'posts': BlogPost.objects.all(),
#     # }
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'blog_index.html', context)


# def blog_category(request, category):
#     # pull from db
#     posts = BlogPost.objects.filter(
#         categories__name__contains=category
#     ).order_by('-created_on')
#     # define context
#     context = {
#         'category': category,
#         'posts': posts
#     }
#     # return rendered html template
#     return render(request, 'blog_category.html', context)

# def blog_detail(request, pk):
#     # object fetch from Post model, by private key for page
#     post = BlogPost.objects.get(pk=pk)
#     # alternative view method
#     # post = get_object_or_404(BlogPost, id=pk)
#     # alternative data method (dict)
#     # data = {
#     #     'post': post,
#     # }
#
#     form = CommentForm()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = Comment(
#                 author=form.cleaned_data['author'],
#                 body=form.cleaned_data['body'],
#                 post=post
#             )
#
#     # filter comments by post
#     comments = Comment.objects.filter(post=post)
#     # define context
#     context = {
#         'post': post,
#         'comments': comments,
#         'form': form,
#     }
#     # return rendered html template.
#     return render(request, 'blog_detail.html', context)
