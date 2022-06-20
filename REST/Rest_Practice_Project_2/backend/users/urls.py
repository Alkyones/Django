from django.urls import path
from . import views


urlpatterns = [
    path('', views.mixinView, name='index'),
    path('user/create/', views.mixinView, name='detail'),  
    path('user/detail/<int:pk>/', views.mixinView, name='detail'),
    path('user/edit/<int:pk>/', views.mixinView, name='edit'),
    path('user/delete/<int:pk>/', views.mixinView, name='delete'),
]

