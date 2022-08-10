from django.contrib import admin
from projects.models import Project


# Register your models here.
# registers projects.Project
class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
