from django.db import models
from django.contrib.auth.models import User # kayitli kullanicalarin oldugu database

# Create your models here.

class Pass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1 , null= False)

    website = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website    # return the name of the pass

