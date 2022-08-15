# discuss_forum/forms.py
# django imports
from django import forms

# local namespace imports
from models import ForumPost


# Mixin for metadata on Forum posts.
class PostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        # Forum Post metadata list
        fields = ['title', 'content', 'categories', 'tags']
        # vehicle metadata mixin
        # vehicle = {
        #     'make': v_make,
        #     'model': v_model,
        #     'year': v_year,
        #     'submodel': v_trim,
        # }
