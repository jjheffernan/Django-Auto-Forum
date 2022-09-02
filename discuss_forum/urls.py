# discuss_forum/urls.py
# django imports
from django.urls import path, include

# local namespace imports
from discuss_forum.views import *

urlpatterns = [
    path('', forum_home, name='forum_home'),
    path('index/', forum_home, name='forum_index'),
    path('detail/<slug>/', forum_detail, name='detail'),
    path('posts/<slug>/', posts, name='posts'),
    path('posts/create/', create_post, name='create_post'),
    path('latest/', latest_posts, name='latest_posts'),
    # path('search', search_result, name='search_result'),
]

