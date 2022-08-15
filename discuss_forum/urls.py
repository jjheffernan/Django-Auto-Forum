# discuss_forum/urls.py
# django imports
from django.urls import path, include

# local namespace imports
from views import *

urlpatterns = [
    path('forum/', forum_home, name='forum'),
]

