from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person


class PersonForm(forms.ModelForm):
    name = forms.CharField(label=False, max_length=100)
    age = forms.IntegerField(label=False)
    class Meta:
        model = Person
        fields = ['name', 'age']
