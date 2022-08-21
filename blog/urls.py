# blog/urls.py

# django imports
from django.urls import path


# local namespace imports
from blog import views

urlpatterns = [
    # path('', views.blog_index, name='blog_index'),
    path('', views.BlogIndexView.as_view(), name='blog_index'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<category>/', views.blog_category, name='blog_category'),
]
