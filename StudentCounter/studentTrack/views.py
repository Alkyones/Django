from django.shortcuts import render, redirect
from .models import LessonModel,StudentModel
from .forms import StudentForm,LessonForm

# Create your views here.
def index(request):
    return render(request, 'studTemps/index.html')


def showRegisteredStudents(request):
    students = StudentModel.objects.all()

    return render(request, 'studTemps/students.html' ,context={'students':students})


def showExistedLessons(request):
    lessons = LessonModel.objects.all()

    return render(request, 'studTemps/lessons.html' ,context={'lessons':lessons})


def addNewStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexPage')
    form = StudentForm()
    return render(request, 'studTemps/addStudent.html', context={'form':form})


def addLesson(request):
    if request.method == 'POST':
        form =LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexPage')
    form = LessonForm()
    return render(request, 'studTemps/addLesson.html', context={'form':form})