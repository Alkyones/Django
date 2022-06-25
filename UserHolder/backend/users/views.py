from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
# Create your views here.

#import models
from .models import UserSave

#import forms
from .forms import UserForm, CustomCreationForm


def index(request):
    return render(request,'base.html')


#register
def register(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})
    

@login_required
def usersList(request):
    data = UserSave.objects.filter(signedUser=request.user)

    return render(request, 'userList.html',context={"users":data})


@login_required
def userAdd(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.instance.signedUser = request.user
            form.save()
            return redirect('userList')

    else:
        form = UserForm()
    return render(request, 'userAdd.html',context={'form':form})


def userDetail(request,pk):
    user = UserSave.objects.get(pk=pk)
    return render(request, 'userDetail.html',{'user':user})


def userDelete(request,pk):
    user = UserSave.objects.get(pk=pk)
    user.delete()
    return redirect('/accounts/profile/')


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)