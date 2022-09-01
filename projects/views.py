# project/views.py
# django imports
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import TemplateView, ListView

from django.contrib.auth.models import User
# local namespace imports
from projects.models import Project


# Create your views here.


# --- app.projects --- #
# turn into class
# Index view of a Specific Project
class ProjectsIndexView(ListView):

    model = Project
    template_name = 'project_index.html'
    context_object_name = 'projects'
    paginate_by = 15

    # def get_queryset(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))


def project_index(request):
    manager_obj = Project.objects  # testing objects call method
    projects = manager_obj.all()  # SQL query

    # define dictionary context
    context = {
        'project': projects
    }  # added as argument to render
    return render(request, 'project_index.html', context)


# turn into class
# Detailed view of a Specific Project
# class ProjectDetailView(DetailView):
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)  # pk is Primary key

    # define dictionary context
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
