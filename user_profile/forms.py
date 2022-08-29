# user_profile/forms.py

# django imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# local namespace imports
from user_profile.models import Profile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # fields = UserCreationForm.Meta.fields + ('email',)
        # in order to use the above fields line, update meta to Meta(UserCreationForm.Meta)


# update user information, Username/email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# Update profile picture
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
