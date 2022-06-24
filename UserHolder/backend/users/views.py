import email
from re import U
from django.shortcuts import render,redirect
# Create your views here.

#import models
from .models import User

#import forms
from .forms import UserForm



def usersList(request):
    users = User.objects.all()
    return render(request, 'userList.html',context={"users":users})



def userAdd(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/')

    else:
        form = UserForm()
    return render(request, 'userAdd.html',context={'form':form})


def userDetail(request,pk):
    user = User.objects.get(pk=pk)
    return render(request, 'userDetail.html',{'user':user})


def userDelete(request,pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('/users/')
