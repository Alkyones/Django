from django.urls import path
from . import views

#/api/products/
urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view(), name='product-detail'),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product-detail'),

    path('', views.ProductListCreateAPIView.as_view(), name='product-list'),

    
]