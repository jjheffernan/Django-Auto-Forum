from django.shortcuts import render
from projects.models import Project


# Create your views here.


# --- app.projects --- #

# Index view of a Specific Project
def project_index(request):
    manager_obj = Project.objects  # testing objects call method
    projects = manager_obj.all()  # SQL query

    # define dictionary context
    context = {
        'project': projects
    }  # added as argument to render
    return render(request, 'project_index.html', context)


# Detailed view of a Specific Project
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)  # pk is Primary key

    # define dictionary context
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
