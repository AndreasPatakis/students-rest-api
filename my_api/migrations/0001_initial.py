# Generated by Django 2.2 on 2021-07-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('home_university', models.CharField(max_length=50)),
                ('outgoing_university', models.CharField(max_length=50)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
    ]