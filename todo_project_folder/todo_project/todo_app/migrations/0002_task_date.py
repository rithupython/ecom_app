# Generated by Django 4.1.7 on 2023-03-06 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2023-03-06'),
            preserve_default=False,
        ),
    ]
