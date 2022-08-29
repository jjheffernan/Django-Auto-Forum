# blog/urls.py

# django imports
from django.urls import path


# local namespace imports
from blog import views

urlpatterns = [
    path('index/', views.BlogIndexView.as_view(), name='blog_index'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('<category>/', views.BlogCategoryView.as_view(), name='blog_category')
    # path('post/create/', views.AddBlog.as_view(), name='create_blog'),
    # path('post/<int:pk>/edit/', views.EditBlog.as_view(), name='edit_blog'),
    # path('post/<int:pk>/delete/', views.DeleteBlog.as_view(), name='delete_blog'),
]

# path('<slug:blog_post>/', views.BlogDetailView.as_view(), name='blog_detail'),

# To use the function based legacy views:
# path('', views.blog_index, name='blog_index'),
# path('<int:pk>/', views.blog_detail, name='blog_detail'),
# path('<category>/', views.blog_category, name='blog_category'),
