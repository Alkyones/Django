from .models import StudentModel,LessonModel

from django.forms import ModelForm
from django import forms



class LessonForm(ModelForm):
    lesson_name = forms.CharField(max_length=100, required=True, label=False,
    widget= forms.TextInput(attrs={'placeholder':'Enter lesson name'}))

    lesson_price = forms.IntegerField(min_value=1 ,required=True, label=False,
    widget= forms.NumberInput(attrs={'placeholder':'Enter lesson price'})) 

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