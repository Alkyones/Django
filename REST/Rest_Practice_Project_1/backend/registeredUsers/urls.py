from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_view, name='create'),
    path('detail/<int:pk>/', views.detail_view, name='detail'),
    path('delete/<int:pk>/', views.delete_view, name='delete'),
    path('update/<int:pk>/', views.update_view, name='update'),
]