from django import forms




class NewListForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter a to-do list'}))


class NewItemForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter a to-do item'}))