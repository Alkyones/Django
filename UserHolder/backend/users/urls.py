from django.urls import  path
from . import views

# 127.0.0.1:8000/users/
urlpatterns = [
   path('', views.usersList,name='userList'),
   path('add/', views.userAdd,name='userAdd'),
   path('detail/<int:pk>/', views.userDetail,name='userDetail'),
   path('delete/<int:pk>/', views.userDelete,name='userDelete'),

]