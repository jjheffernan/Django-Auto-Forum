# test_page/urls.py
# django imports
from django.urls import path
# local namespace imports
from test_page.views import *

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('test_exc', test_page, name='test_view'),
]
