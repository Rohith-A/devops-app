# Generated by Django 4.2.5 on 2023-12-11 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_alter_todoitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
