# Generated by Django 4.2 on 2023-04-17 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasktracker', '0005_task_task_completed_task_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_priority',
            field=models.CharField(choices=[('red', 'RED'), ('yellow', 'YELLOW'), ('green', 'GREEN')], default='red', max_length=20, null=True),
        ),
    ]
