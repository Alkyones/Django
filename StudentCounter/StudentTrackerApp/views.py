from itertools import count
from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    count = 2
    
    return render(request,'index.html',context={'count':count})

def add_student(request):
    global count
    count += 1
        