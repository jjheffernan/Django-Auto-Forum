# blog/forms.py
# django imports
from django import forms

# local namespace imports
from blog.models import Post


# Blog post edit form
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name'
        })
    )
    # need to change to add "" since these are delivered to user
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Leave a Comment Here'
        }
    ))


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
