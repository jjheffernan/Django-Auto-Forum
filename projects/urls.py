# project/urls.py

# django imports
from django.urls import path
from projects.views import *  # imports project views from app

urlpatterns = [
    # path('', project_index, name='project_index'),
    path('', ProjectsIndexView.as_view(), name='project_index'),
    # path('<int:pk>/', project_detail, name='project_detail'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]

