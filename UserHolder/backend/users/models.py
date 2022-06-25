from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserSave(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    signedUser = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return "%s (username: %s)" % (self.username, self.email)