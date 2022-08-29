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


class PwdChangeForm(PasswordChangeForm):

    old_password = forms.CharField(
        label='Old Password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3',
                   'placeholder': 'Old Password',
                   'id': 'form-oldpass'}))
    new_password1 = forms.CharField(
        label='New Password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3',
                   'placeholder': 'New Password',
                   'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3',
                   'placeholder': 'New Password',
                   'id': 'form-newpass2'}))


# Reset password form
class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3',
               'placeholder': 'Email',
               'id': 'form-email'}
    ))

    def clean_email(self):
        email = self.cleaned_data['email']
        # can also try: email = self.clean_email(self)

        test = User.objects.filter(email=email)
        if not test:
            raise forms.ValidationError('Invalid email address, please register.')
        return email

# -- Accont Creation Forms --


# Admin/Custom User Creation (non-standard roles)
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

    first_name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3',
                   'placeholder': 'Firstname',
                   'id': 'form-firstname'}))
    last_name = forms.CharField(
        label='Lastname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3',
                   'placeholder': 'Lastname',
                   'id': 'form-lastname'}))
    email = forms.EmailField(
        max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3',
                   'placeholder': 'Update Email',
                   'id': 'form-email'}))

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_name'].required = False
        self.fields['email'].required = False


# Update profile picture
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['bio', 'image']  # for profile photos

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'})
        }


class RegistrationForm(forms.ModelForm):

    username = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required',
                             error_messages={
                                 'required': 'Invalid email, please put in an email to proceed'
                             })

    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_pwd2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Username is taken')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-3',
             'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3',
             'placeholder': 'Email',
             'name': 'email',
             'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Repeat Password'})
