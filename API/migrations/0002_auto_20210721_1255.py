# Generated by Django 2.2 on 2021-07-21 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='StudentData',
        ),
    ]