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

# register Comments
class CommentAdmin(admin.ModelAdmin)
    list_display = ('author', 'body', 'post', 'created_on')
    # potential additional fields: 'active', 'status'
    # search_fields = ()

    def approve_comments(self, request, queryset):
        queryset.update(active=False)

    def hide_comments(self, request, queryset):
        queryset.update(active=False)


# this is an alternative method, should generalize all post methods
# @admin.register(Post)
# class BlogAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title',), }


# Registers file to site
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)

