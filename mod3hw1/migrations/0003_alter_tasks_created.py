# Generated by Django 4.1.5 on 2023-01-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mod3hw1', '0002_alter_tasks_complited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created',
            field=models.DateTimeField(auto_now=True, help_text='дата и время создания'),
        ),
    ]
