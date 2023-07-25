from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from .forms import *
from .models import *


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # Take the entered data and creat a form
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password, email=email)
            # Select every field you need for authentication

            if user is not None:
                login(request, user)
                user_profile, created = UserLoginModel.objects.get_or_create(user=user)
                user_profile.save()
                return redirect('home')
            # if not user.is_active:
            #     print('Your account is not activated.')
    else:
        form = LoginForm()  # Then create a empty form and show it to user

    context = {
        'form': form
    }

    return render(request, 'appAuthentication/login.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'appAuthentication/logout.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)  # Commit=False ables us to add more attribute
            user.is_active = True  # This helps us not to let users login until they are confirmed the email
            user.refresh_from_db()  # Since the above commit is False we cannot run this piece of code
            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()

    context = {
        'form': form,

    }
    return render(request, 'appAuthentication/signup.html', context)
