from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput)


class SignupForm(UserCreationForm):

    class Meta:
        model = User  # This model is not necessary to be added via from django.contrib.auth.models import User
        fields = ('username', 'email', 'password1', 'password2', )  # With User Model, we can only add fields that are
        # defined in the built-in User Model
