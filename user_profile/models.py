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
    profile_img = models.ImageField(default='default.jpg', upload_to='profile_pics')  # profile image integration

    def __str__(self):
        return f'{self.user}.Profile'

    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_pic = (300, 300)
    #         img.thumbnail(output_pic)
    #         img.save(self.image.path)
