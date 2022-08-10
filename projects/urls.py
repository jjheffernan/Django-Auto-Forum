from django.urls import path
from . import views  # imports project views from app

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('<int:pk/', views.project_detail, name='project_detail'),
]

