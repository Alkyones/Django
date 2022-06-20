from django.contrib import admin
from .models import NewListModel, NewItemModel
# Register your models here.
# admin.site.register(ModelName)

admin.site.register(NewListModel)
admin.site.register(NewItemModel)
