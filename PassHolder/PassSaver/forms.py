from django.forms import ModelForm
from .models import Pass


class PassForm(ModelForm):
    class Meta:
        model = Pass
        fields = ['website','username', 'password']