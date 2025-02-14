# Create your views here.
from django.shortcuts import render
from .models import Product

from django.db.models import DecimalField

def even_prices(request):
    products = Product.objects.extra(where=["CAST(price as integer) % 2 = 0"])
    return render(request, 'products.html', {'products': products})

def odd_prices(request):
    products = Product.objects.extra(where=["CAST(price as integer) % 2 = 1"])
    return render(request, 'products.html', {'products': products})


def show_all(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})