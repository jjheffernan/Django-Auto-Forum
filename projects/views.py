from django.shortcuts import render
from projects.models import Project


# Create your views here.
def project_index(request):
    projects = Project.objects.all()  # SQL query
    context = {
        'projects': projects
    }  # added as argument to render
    return render(request, 'project_index.html', context)

