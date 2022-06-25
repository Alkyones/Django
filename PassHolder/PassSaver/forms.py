from django.forms import ModelForm, TextInput
from .models import Pass
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class PassForm(ModelForm):
    class Meta:
        model = Pass
        fields = ['website','username', 'password']

class registerForm(UserCreationForm):
    username = forms.CharField(max_length=255,label=False, widget=forms.TextInput(attrs={'placeholder':'Please enter a username'}))
    password1 = forms.CharField(max_length=255,label=False, widget=forms.PasswordInput(attrs={'placeholder':'Please enter a password'}))
    password2 = forms.CharField(max_length=255,label=False,help_text=False, widget=forms.PasswordInput(attrs={'placeholder':'confirmate your password'}))

    class Meta:
        model = User
        fields = ['username', 'password1','password2']  