from django.forms import ModelForm
from numpy import signedinteger
from .models import UserSave
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(ModelForm):
    username = forms.CharField(max_length=255,label=False, required=True,
    widget=forms.TextInput(attrs={'class': 'form-control','autocomplete': 'OFF','placeholder': 'Enter  your username...'}))

    email = forms.EmailField(max_length=255,label=False, required=True,
    widget=forms.EmailInput(attrs={'class': 'form-control','autocomplete': 'OFF', 'placeholder': 'Enter  your email...'}))

    password = forms.CharField(max_length=255,label=False, required=True,
    widget=forms.PasswordInput(attrs={'class': 'form-control','autocomplete': 'OFF', 'placeholder': 'Enter  your password...'}))
    class Meta:
        model = UserSave
        fields = ['username', 'email', 'password']


class CustomCreationForm(UserCreationForm):
    username = forms.CharField(max_length=255,label=False, required=True,
    widget=forms.TextInput(attrs={'class': 'form-control','autocomplete': 'OFF','placeholder': 'Enter  your username...'}))

    email = forms.EmailField(max_length=255,label=False, required=True,
    widget=forms.EmailInput(attrs={'class': 'form-control','autocomplete': 'OFF', 'placeholder': 'Enter  your email...'}))

    password1 = forms.CharField(max_length=255,label=False, required=True,
    widget=forms.PasswordInput(attrs={'class': 'form-control','autocomplete': 'OFF', 'placeholder': 'Enter  your password...'}))

    password2 = forms.CharField(max_length=255,label=False, required=True,
    widget=forms.PasswordInput(attrs={'class': 'form-control','autocomplete': 'OFF', 'placeholder': 'Enter  your password...'}))

    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']
    