from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    acc_name = models.CharField(max_length=50)

    def __str__(self):
        return self.acc_name

class Task(models.Model):
    FLAGS = (
        ('red', 'RED'),
        ('yellow', 'YELLOW'),
        ('green', 'GREEN')
    )
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200, null=False)
    task_description = models.CharField(max_length=200, null=False)
    task_date = models.DateField()
    task_completed = models.BooleanField(null=True, default=False)
    task_priority = models.CharField(max_length=20, null=True, choices=FLAGS, default='yellow')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name