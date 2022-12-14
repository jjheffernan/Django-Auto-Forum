# discuss_forum/admin.py

# django imports
from django.contrib import admin

# local namespace imports
from discuss_forum.models import *

# Register your models here.

admin.site.register(ForumCategory)
admin.site.register(ForumPost)
admin.site.register(ForumComment)
admin.site.register(Author)
admin.site.register(Reply)
