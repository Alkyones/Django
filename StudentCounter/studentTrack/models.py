from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    ADMIN = 1
    STUDENT = 2
    TEACHER = 3

    ROLE_CHOICES = (
        (TEACHER, 'teacher'),
        (STUDENT, 'student'),
        (ADMIN, 'admin'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True )




class StudentModel(models.Model):
    class genders(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
        NonBinary = 'nonbinary', "Don't want to answer"

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=100)    
    age = models.IntegerField()
    gender = models.CharField(
        max_length=20,
        choices=genders.choices,
        default=genders.NonBinary
    )

    isverified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.email}'


class LessonModel(models.Model):
    lesson_name = models.CharField(max_length=100, unique=True)
    lesson_price = models.IntegerField()

    def __str__(self):
        return f'{self.lesson_name} - {self.lesson_price}'