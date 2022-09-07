# discuss_forum/urls.py
# django imports
from django.urls import path, include

# local namespace imports
from discuss_forum.views import *

urlpatterns = [
    path('', forum_home, name='forum_home'),  # function view
    path('index/', ForumHome.as_view(), name='forum_index'),  # class view
    path('detail/<slug>/', forum_post_detail, name='detail'),
    path('posts/<slug>/', posts, name='posts'),
    path('posts/create/', create_post, name='create_post'),
    path('create/', create_post, name='create_post'),
    path('latest/', latest_posts, name='latest_posts'),
    # path('search', search_result, name='search_result'),
]

