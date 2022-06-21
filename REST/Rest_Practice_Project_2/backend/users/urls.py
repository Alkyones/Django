from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', obtain_auth_token),
    path('user/', views.mixinView, name='index'),
    path('user/create/', views.mixinView, name='detail'),  
    path('user/detail/<int:pk>/', views.mixinView, name='detail'),
    path('user/edit/<int:pk>/', views.mixinView, name='edit'),
    path('user/delete/<int:pk>/', views.mixinView, name='delete'),
]

