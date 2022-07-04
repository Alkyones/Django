"""cfmain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from users import views
# 127.0.0.1:8000\
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register,name='register'),

    #apps
    path('users/', include('users.urls')),
    path('forum/', include('chatbot.urls')),
    path('accounts/profile/', views.usersList,name='userList'),

]

handler404 = "users.views.page_not_found_view"