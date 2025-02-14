from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def is_even(self):
        return self.price % 2 == 0

    def is_odd(self):
        return self.price % 2 != 0