# user_profile/urls.py
# django imports
from django.conf.urls import path

# local app imports
from user_profile.views import dashboard

urlpatterns = [
    path(r'^dashboard/', dashboard, name='dashboard')
]
# remember to change to class.as_view later on
