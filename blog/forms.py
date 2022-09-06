# blog/forms.py
# django imports
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# local namespace imports
from blog.models import Post


# Blog post edit form
class BlogPostForm(forms.ModelForm):
    # see models.py for fields
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.Form, LoginRequiredMixin):
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
        fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


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
