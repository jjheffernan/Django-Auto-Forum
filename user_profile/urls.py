# user_profile/urls.py
# django imports
from django.urls import path, include


# local app imports
from user_profile import views

urlpatterns = [
    path(r'accounts/', include("django.contrib.auth.urls")),
    path(r'dashboard/', views.dashboard, name='dashboard'),
    path(r'register/', views.register, name='register'),
    path(r'profile/', views.profile, name='profile'),
]
# remember to change to class.as_view later on
# see user_profile/README.md for notes on "django.contrib.auth.urls"
