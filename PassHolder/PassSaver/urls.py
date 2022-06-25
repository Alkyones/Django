from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('add/', views.showPassword, name='add'),
    path('register/', views.register, name='register'),
    path('', include('django.contrib.auth.urls'))   ]