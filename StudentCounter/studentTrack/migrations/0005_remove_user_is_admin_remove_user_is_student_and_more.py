# Generated by Django 4.0.4 on 2022-09-02 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentTrack', '0004_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_teacher',
        ),
    ]
