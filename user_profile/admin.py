# user_profile/admin.py

# django imports
from django.contrib import admin

# local namespace imports
from user_profile.models import Profile

# Register your models here.

admin.site.register(Profile)
