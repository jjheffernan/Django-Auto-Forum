# user_profile/views.py
# django imports
from django.shortcuts import render


# Create your views here.
# dashboard view (function based)
def dashboard(request, pk):
    return render(request, 'user_profile/dashboard.html')
