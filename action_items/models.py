from unittest.util import _MAX_LENGTH
from django.db import models

class Status:
    NEW = "New"
    INPROGRESS = "InProgress"
    COMPLETE = "Complete"
    STALLED = "Stalled"
    DISCONTINUED = "Discontinued"

# Create your models here.
class TaskProject(models.Model):
    client=models.CharField(max_length=100)
    project_name=models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    deadline = models.DateField()
    progress = models.IntegerField()
    created_on=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        return f"{self.client} : {self.project_name}"
    
    def __str__(self) -> str:
        return f"{self.client} : {self.project_name}"

class Task(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField()    
    status = models.CharField(max_length=100)
    deadline = models.DateField()
    progress = models.IntegerField()
    created_on=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)
    task_project = models.ForeignKey('TaskProject', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} | {self.description[:10]}"

class Comment(models.Model):
    comment=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)
    task=models.ForeignKey('Task',on_delete=models.CASCADE)