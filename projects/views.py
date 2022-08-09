from django.shortcuts import render
from projects.models import Project


# Create your views here.


# --- app.projects --- #

# Index view of a Specific Project
def project_index(request):
    projects = Project.objects.all()  # SQL query
    context = {
        'projects': projects
    }  # added as argument to render
    return render(request, 'project_index.html', context)


# Detailed view of a Specific Project
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)  # pk is Primary key
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
