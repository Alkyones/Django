from django.contrib import admin
from .models import LessonModel, StudentModel,User
# Register your models here.

admin.site.register(User)

admin.site.register(LessonModel)
admin.site.register(StudentModel)