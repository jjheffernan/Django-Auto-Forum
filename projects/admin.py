# projects/admin.py
# django imports
from django.contrib import admin

# local namespace imports
from projects.models import Project


# Register your models here.
# registers projects.Project
class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
