# Generated by Django 4.0.4 on 2022-08-28 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentTrack', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmodel',
            old_name='student_age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='studentmodel',
            old_name='student_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='studentmodel',
            old_name='student_gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='studentmodel',
            old_name='student_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='studentmodel',
            old_name='student_phone',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='isverified',
            field=models.BooleanField(default=False),
        ),
    ]
