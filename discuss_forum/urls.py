# discuss_forum/urls.py
# django imports
from django.urls import path, include

# local namespace imports
from views import *

urlpatterns = [
    path('forum/', forum_home, name='forum'),
    path('detail/<slug>/', forum_detail, name='detail'),
    path('posts/<slug>/', posts, name='posts'),
    path('create_post', create_post, name='create_post'),
    path('latest_posts', latest_posts, name='latest_posts'),
    # path('search', search_result, name='search_result'),
]

