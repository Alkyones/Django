from django.shortcuts import render
from .forms import PersonForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def personPage(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form = PersonForm()
    return render(request, 'personPage.html', {'form': form})