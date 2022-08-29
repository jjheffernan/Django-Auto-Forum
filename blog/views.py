# blog/views.py

# django imports
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# local namespace imports
from blog.models import Post, Comment
from blog.forms import CommentForm


# Create your views here.

# Index View
class BlogIndexView(ListView):

    # declare variables here
    model = Post
    template_name = "blog_index.html"
    context_object_name = 'posts'
    # context_object_name = 'blog_list'  # alternative object in ORM
    # paginate_by = 2
    # ordering = [-date_posted']

    # def __str__(self):
    #     # this is part of the initialization of a view
    #     return self.template_name

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['posts'] = Post.objects.all()
    #     return context


# Category View
class BlogCategoryView(ListView):
    model = Post
    template_name = 'blog_category.html'
    context_object_name = 'posts'
    # context_object_name = 'blog_cat_list'  # alternative object in ORM
    # paginate_by = 2

    # method override does not work, needs to return category as title
    # def get_queryset(self):
    #     content = {
    #         'cat': self.kwargs['category'],
    #         'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='published')
    #     }
    #     return Post.objects.filter(blog_category__icontains=self.kwargs.get('categories'))
    #     return content
    # when not overwritten, site displays but without header

    # may need to add get_context_data
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['category'] = get_object_or_404(Post, category=self.kwargs.get('category'))
    #     context['posts'] = get_object_or_404(Post, pk=self.kwargs.get('pk'))


# blog detail view
class BlogDetailView(DetailView):

    model = Post
    template_name = "blog_detail.html"
    form = CommentForm()
    context_object_name = 'post'
    # pk_url_kwarg = 'custom_pk'

    def __str__(self):
        return Post.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['posts'] = Post.objects.filter(id=self.kwargs.get('id'))
        context['posts'] = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        return context

    def post(self, request):
        Comment.object.create()


# CRUD method classes for Blog Posts
# Create New Blog Post
class AddBlog(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_blog.html'
    fields = '__all__'
    success_url = reverse_lazy('blog:posts')  # unsure if correct syntax, check docs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Edit Existing Blog Post
class EditBlog(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'edit_blog.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blog:posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Delete Existing Blog Post
class DeleteBlog(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blog:posts')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# legacy function based views

# def blog_index(request):
#     posts = Post.objects.all().order_by('-created_on')  # by changing to class oriented, this can be separated
#     # objects is a bad call
#     # alternative data call
#     # data = {
#     #     'posts': Post.objects.all(),
#     # }
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'blog_index.html', context)


# def blog_category(request, category):
#     # pull from db
#     posts = Post.objects.filter(
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
#     post = Post.objects.get(pk=pk)
#     # alternative view method
#     # post = get_object_or_404(Post, id=pk)
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
