from .models import StudentModel, LessonModel,User
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from django import forms


from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate','placeholder': 'Email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))


class LessonForm(ModelForm):
    lesson_name = forms.CharField(max_length=100, required=True, label=False,
                                  widget=forms.TextInput(attrs={'placeholder': 'Enter lesson name'}))

    lesson_price = forms.IntegerField(min_value=1, required=True, label=False,
                                      widget=forms.NumberInput(attrs={'placeholder': 'Enter lesson price'}))

    class Meta:
        model = LessonModel
        fields = ['lesson_name', 'lesson_price']


class StudentForm(ModelForm):
    
    name = forms.CharField(max_length=255, label=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Student Name'}))

    email = forms.EmailField(max_length=255, label=False,
                             widget=forms.EmailInput(attrs={'placeholder': 'Student Email'}))

    age = forms.IntegerField(min_value=18, max_value=100, label=False,
                             widget=forms.NumberInput(attrs={'placeholder': 'Student age'}))

    class Meta:
        
        model = StudentModel
        fields = ['name', 'email', 'age', 'gender']

        labels = {
            'gender': ''
        }
        help_texts = {
            'gender': 'Select your gender',
        }


class NewUserForm(UserCreationForm):
    ADMIN = 1
    STUDENT = 2
    TEACHER = 3

    ROLE_CHOICES = (
        (TEACHER, 'teacher'),
        (STUDENT, 'student'),
        (ADMIN, 'admin'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user