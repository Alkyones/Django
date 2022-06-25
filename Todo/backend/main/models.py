from django.db import models
from django.conf import settings


# Create your models here.

class NewListModel(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.user}"


class NewItemModel(models.Model):
    text = models.CharField(max_length=100)
    listKey = models.ForeignKey(NewListModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.text