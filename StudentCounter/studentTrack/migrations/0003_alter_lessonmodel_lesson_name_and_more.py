# Generated by Django 4.0.4 on 2022-08-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentTrack', '0002_rename_student_age_studentmodel_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonmodel',
            name='lesson_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('nonbinary', "Don't want to answer")], default='nonbinary', max_length=20),
        ),
    ]