# user_profile/forms.py

# django imports
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# local namespace imports
from user_profile.models import Profile

# some links to relevant docs for what is null value on init and what is not
# https://docs.djangoproject.com/en/3.0/topics/forms/
# https://docs.djangoproject.com/en/3.0/topics/auth/default/


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3',
                   'placeholder': 'New Password',
                   'id': 'form-newpass'}
        )
    )
    new_password2 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3',
                   'placeholder': 'Confirm Password',
                   'id': 'form-newpass2'}
        )
    )


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3',
               'placeholder': 'Username',
               'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password',
            'id': 'login-pwd',
        }
    ))




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
