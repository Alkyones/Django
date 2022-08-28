from django.contrib import admin
from .models import LessonModel, StudentModel
# Register your models here.


admin.site.register(LessonModel)
admin.site.register(StudentModel)