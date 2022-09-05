# user_profile/views.py

# django imports
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.views.generic import View, TemplateView, CreateView

# local imports
from user_profile.forms import *
from user_profile.models import Profile


# Create your views here.

User = get_user_model()


# dashboard view (class based)
@login_required
class ProfileDashboard(TemplateView):
    template_name = 'user_dashboard.html'
    model = User


# dashboard view (function based)
def dashboard(request):
    return render(request, 'registration/login_dashboard.html')


# THIS LENDS ITSELF VERY NICELY TO CBVs
# START HERE
class RegisterProfile(CreateView):
    model = User
    template_name = 'registration/register.html'
    # success_url = reverse_lazy('login')
    form_class = UserRegisterForm


def register(request):
    if request.method == "GET":
        return render(request, 'registration/register.html',
                      {'form': CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)  # does not immediately save
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # a backend associated with user, then saves db

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')  # logs the registration on backend/ admin

            user.save()
            login(request, user)
            return redirect(reverse('dashboard'))
        else:
            form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': CustomUserCreationForm})


# profile page (class based)
class ProfilePage(View):
    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    def post(self, request):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # abstract this out for security, similar to comments
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')


# profile page (function based)
@login_required
def profile(request):

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # abstract this out for security, similar to comments
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'profile.html', context)
