# Generated by Django 4.2.5 on 2023-12-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
