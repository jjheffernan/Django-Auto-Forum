# user_profile/models.py
# django imports
from django.db import models
from django.contrib.auth.models import User

# local namespace imports
# none


# Create your models here.
# base user profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_img = models.ImageField(default='default.jpg', upload_to='profile_pics')  # profile image integration

    # def __str__(self):
    #     return f'{self.user.} Profile'
