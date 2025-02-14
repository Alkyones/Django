import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LINQ.settings")

import django
django.setup()


import random
from products.models import Product

for i in range(20):
    name = f"Product {i+1}"
    price = random.randint(10, 50)
    Product.objects.create(name=name, price=price)
