from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Pass
from .forms import PassForm,registerForm


# Create your views here.
def index(request):
    #get - data cekmek - request.user.is_authenticated
    # post - data vermek
    # put - data guncellemek
    # retrieve  - spesifik data alimi icin kullanilir
    # destroy -  data silmek icin kullanilir - request.user.is_superuser Only
    print(request.user)
    print(request.user.is_authenticated)
    print(request.user.is_staff)
    print(request.user.is_superuser)
    return render(request, 'main.html')

def showPassword(request):
    if request.method == 'GET':
        form = PassForm()
        passwords = Pass.objects.filter(user=request.user)
    elif request.method == 'POST':
        form = PassForm(request.POST)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponse('<h1>Password added!</h1>')
        else:
            return HttpResponse('<h1>Invalid form!</h1>')
        
    return render(request, 'showPassword.html', {'passwords': passwords, 'form': form})

def deletePassword(request,pk):
    item = Pass.objects.filter(pk =pk)
    item.delete()
    return redirect('add')

def updatePassword(request,pk):
    if request.method == 'POST':
        form = PassForm(request.POST)
        if form.is_valid():
            Pass.objects.filter(pk=pk).update(
                user=request.user,
                website = request.POST.get('website'),
                username = request.POST.get('username'),
                password = request.POST.get('password'),
                # ?
            )
        return redirect('add')
    
    form = PassForm()
    return render(request,'updatePassword.html', {'form': form})

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
        

