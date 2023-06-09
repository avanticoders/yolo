# Generated by Django 4.2 on 2023-04-17 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasktracker', '0004_alter_task_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_completed',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='task_priority',
            field=models.CharField(choices=[('red', 'RED'), ('yellow', 'YELLOW'), ('green', 'GREEN')], max_length=20, null=True),
        ),
    ]
