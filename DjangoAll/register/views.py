from django.shortcuts import render,redirect
from .forms import registrationForm
def register(response):
    if response.method == 'POST':
        form = registrationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/main/home')
    else:
        form = registrationForm()
    return render(response, 'register.html', {'form': form})