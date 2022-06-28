from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('add/', views.showPassword, name='add'),
    path('delete/<int:pk>/',views.deletePassword, name='delete'),
    path('update/<int:pk>/',views.updatePassword, name='update'),

    path('register/', views.register, name='register'),
    path('', include('django.contrib.auth.urls'))   ]