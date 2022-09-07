# user_profile/urls.py
# django imports
from django.urls import path, include


# local app imports
from user_profile.views import *

urlpatterns = [
    path(r'accounts/', include("django.contrib.auth.urls")),
    path(r'dashboard/', dashboard, name='dashboard'),
    # path(r'user_home/', ProfileDashboard.as_view, name='user_dashboard'),
    # path(r'register/', register, name='register'),
    path(r'register/', RegisterProfile.as_view(), name='register'),
    path(r'profile/', ProfilePage.as_view(), name='profile'),
    # path(r'profile/', views.profile, name='profile'),
]
# remember to change to class.as_view later on
# see user_profile/README.md for notes on "django.contrib.auth.urls"
