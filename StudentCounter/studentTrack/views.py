from django.shortcuts import render, redirect
from .models import LessonModel,StudentModel
from .forms import StudentForm,LessonForm,NewUserForm

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def index(request):
    return render(request, 'studTemps/index.html')


@login_required(login_url='/login')
def showRegisteredStudents(request):
    if request.method == 'POST':
        students = StudentModel.objects.filter(name__icontains=request.POST.get('name'))
    else:
        students = StudentModel.objects.all()

    return render(request, 'studTemps/students.html' ,context={'students':students})


def showExistedLessons(request):
    if request.method == 'POST':
        lessons=LessonModel.objects.filter(lesson_name__icontains=request.POST.get('lessonSearch'))
    else:
        lessons = LessonModel.objects.all()

    return render(request, 'studTemps/lessons.html' ,context={'lessons':lessons})


@login_required(login_url='/login')
def addNewStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexPage')
    form = StudentForm()
    return render(request, 'studTemps/addStudent.html', context={'form':form})

@login_required(login_url='/admin')
def addLesson(request):
    if request.method == 'POST':
        form =LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexPage')
    form = LessonForm()
    return render(request, 'studTemps/addLesson.html', context={'form':form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexPage')
    form = NewUserForm()
    return render(request, 'registration/register.html', {'form': form})