from django.urls import path
from StudentTrackerApp import views

urlpatterns = [
    path('main', views.index, name='main'),
    path('main', views.add_student , name='add'),
]