# user_profile/forms.py

# django imports
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# local namespace imports
from user_profile.models import Profile


class CustomUserCreationForm(UserCreationForm):
    # This will eventually will be for admin creation and management of user profiles
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
        fields = ['bio', 'image']  # for profile photos

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'})
        }
