from django import forms

class CreateNewListForm(forms.Form):
    name = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'placeholder':'Enter the name of the list','class':'form-control','style':'width:80%'}))



