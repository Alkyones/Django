from logging import PlaceHolder
from tabnanny import verbose
from django.forms import ModelForm
from .models import User
from django import forms

class UserForm(ModelForm):
    username = forms.CharField(max_length=255,label=False, required=True,
    widget=forms.TextInput(attrs={'class': 'form-control','autocomplete': 'OFF','placeholder': 'Enter  your username...'}))

    email = forms.EmailField(max_length=255,label=False, required=True,
    widget=forms.EmailInput(attrs={'class': 'form-control','autocomplete': 'OFF', 'placeholder': 'Enter  your email...'}))

    password = forms.CharField(max_length=255,label=False, required=True,
    widget=forms.PasswordInput(attrs={'class': 'form-control','autocomplete': 'OFF', 'placeholder': 'Enter  your password...'}))
    class Meta:
        model = User
        fields = '__all__'
        