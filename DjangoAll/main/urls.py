from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.lists , name='lists'),
    path('list/<int:id>/', views.ListDesc , name='ListDescription'),
    path('home/', views.home , name='home'),
    path('create/', views.create , name='create'),


]