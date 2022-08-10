from django.contrib import admin
from blog.models import Post, Category


# Register your models here.
# register blog.PostAdmin
class PostAdmin(admin.ModelAdmin):
    pass


#
class CategoryAdmin(admin.ModelAdmin):
    pass


# Registers file to site
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

