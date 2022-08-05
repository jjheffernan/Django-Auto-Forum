from django.urls import path
from test_page import views

urlpatterns = [
    path('test_error/', views.test_page, name='test_page')
]
