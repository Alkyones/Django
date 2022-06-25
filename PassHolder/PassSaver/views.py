from django.shortcuts import render
from django.http import HttpResponse
from .models import Pass
from .forms import PassForm,registerForm


# Create your views here.
def index(request):
    return render(request, 'main.html')

def showPassword(request):
    if request.method == 'GET':
        form = PassForm()
        passwords = Pass.objects.all
    elif request.method == 'POST':
        form = PassForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Password added!</h1>')
        else:
            return HttpResponse('<h1>Invalid form!</h1>')
        
    return render(request, 'showPassword.html', {'passwords': passwords, 'form': form})

def register(request):
    if request.method == 'GET':
        form = registerForm()
       
    elif request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>User created</h1>')
        else:
            return HttpResponse('<h1>Invalid form!</h1>')
    return render(request, 'registration.html',{'form': form})
        

