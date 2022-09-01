# blog/admin.py
# django imports
from django.contrib import admin

# local namespace imports
from blog.models import *


# Register your models here.
# register blog.PostAdmin
class PostAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title',), }
    pass


# register categories
class CategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title',), }
    pass


# this is an alternative method, should generalize all post methods
# @admin.register(Post)
# class BlogAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title',), }


# Registers file to site
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

