# Generated by Django 4.0.1 on 2022-04-02 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newitemmodel',
            old_name='list',
            new_name='listKey',
        ),
    ]
