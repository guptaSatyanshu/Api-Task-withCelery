from django.db import models



# Create your models here.



Ctype = [
    ('perday', 'per day'),
    ('weekly', 'weekly'),
    ('monthly', 'monthly'),
]


class Task(models.Model):
    task_type = models.IntegerField()
    task_desc = models.CharField(max_length=300)


class TaskTracker(models.Model):
    task_type = models.ForeignKey(Task, on_delete=models.CASCADE)
    update_type = models.CharField(choices=Ctype, max_length=10)
    email = models.EmailField(unique=True)
