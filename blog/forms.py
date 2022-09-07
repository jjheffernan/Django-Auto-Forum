# blog/forms.py
# django imports
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
# local namespace imports
from blog.models import Post


# Blog post edit form
class BlogPostForm(forms.ModelForm):
    # see models.py for fields
    class Meta:
        model = Post
        fields = '__all__'


# comment form, get_context_data requires CommentForm to be a child of LoginRequiredMixin
# @login_required
class CommentForm(forms.Form):
    # may need to add provision for author
    # need to change to add "" since these are delivered to user
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Leave a Comment Here'
        }
    ))

    class Meta:
        model = Post
        fields = ('post', 'author')

    # def get_context_data(self, **kwargs):
    #     # may need to change this for the login_required flag instead
    #     context = super().get_context_data(**kwargs)
    #
    #     return context


# legacy comment form
# class CommentForm(forms.Form):
#     author = forms.CharField(
#         max_length=60,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Your Name'
#         })
#     )
#     # need to change to add "" since these are delivered to user
#     body = forms.CharField(widget=forms.Textarea(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Leave a Comment Here'
#         }
#     ))
