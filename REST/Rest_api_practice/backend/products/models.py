from django.db import models
from django.conf import settings
# Create your models here.


User = settings.AUTH_USER_MODEL
class Product(models.Model):
    #foreign key
    user = models.ForeignKey(User,null = True, on_delete=models.SET_NULL,)


    title = models.CharField(max_length=120)    
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    
    @property
    def sale_price(self):
        return round(float(self.price) * .8, 2)
    

    def get_discount (self):
        return self.price