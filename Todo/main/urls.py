from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('show/<str:listName>/',views.showListItems, name='show'),
    path('show/',views.showList, name='showList'),
    path('create/',views.createList, name='createList'),


]
