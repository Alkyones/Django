from django.shortcuts import render
from .models import MessageUserModel
from .forms import MessageForm
from django.shortcuts import render,redirect
# Create your views here.


#crud based chatbot between users

def ShowMessages(request):
    messages = MessageUserModel.objects.all().order_by('-id')[:100]
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            form = MessageForm()
    else:
        form = MessageForm()

    
    return render(request, 'chatbox/messages.html',{
        'form': form,
        'messages':messages}
        )