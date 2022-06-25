from django.shortcuts import render,redirect
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/main/home')
    register_form = UserRegisterForm()
    return render(request, 'register/register.html',{'form':register_form})