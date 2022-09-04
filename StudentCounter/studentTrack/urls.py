from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='indexPage' ),

    path('students/', views.showRegisteredStudents, name='students' ),
    path('lessons/', views.showExistedLessons, name='lessons' ),

    path('students/new/', views.addNewStudent, name='addStudent' ),
    path('lessons/new/', views.addLesson, name='addLesson' ),

    

    #Authenticatiom
    path('register/', views.register_request, name='register')
]