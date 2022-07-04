from django.forms import ModelForm
from .models import MessageUserModel



class MessageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['message'].label = ''

    class Meta:
        model = MessageUserModel
        fields = ['message'] 