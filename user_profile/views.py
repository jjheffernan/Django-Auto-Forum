# user_profile/views.py

# django imports
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse

# local imports
from user_profile.forms import CustomUserCreationForm


# Create your views here.
# dashboard view (function based)
def dashboard(request):
    return render(request, 'dashboard.html')


# THIS LENDS ITSELF VERY NICELY TO CBVs
# START HERE
def register(request):
    if request.method == "GET":
        return render(request, 'user_profile/register.html',
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
    return render(request, 'user_profile/register.html', {'form': CustomUserCreationForm})
