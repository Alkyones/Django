from django.db import models
from django.conf import settings
from django.db.models import Q
# Create your models here.


User = settings.AUTH_USER_MODEL

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title_icontains = query ) | Q(content_icontains = query)
        qs = self.is_public.filter(lookup)
        if user is not None:
            qs = qs.filter(user=user)
        return qs

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using= self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)

class Product(models.Model):
    #foreign key
    user = models.ForeignKey(User,null = True, on_delete=models.SET_NULL,)


    title = models.CharField(max_length=120)    
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    public = models.BooleanField(default=True)
    objects= ProductManager()
    @property
    def sale_price(self):
        return round(float(self.price) * .8, 2)
    

    def get_discount (self):
        return self.price