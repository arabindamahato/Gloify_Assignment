from django.db import models
from task.models import *

# Create your models here.

class Task(models.Model):
    task_title = models.CharField(max_length=120, primary_key=True)
    description = models.CharField(max_length=1000)
    end_date = models.CharField(max_length=20)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.task_title 

class Comment(models.Model):
    task_title = models.ForeignKey(Task, on_delete=models.CASCADE)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.task_title)
    
    




