# Generated by Django 4.1.7 on 2023-03-08 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasktracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_date',
            field=models.CharField(max_length=200),
        ),
    ]
