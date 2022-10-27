from django.shortcuts import render,redirect
from .models import Task,TaskProject,Status

def view_all_tasks(request,status_pk:int):
    status=Status.objects.get(pk=status_pk)
    tasks=Task.objects.filter(status=status)
    return render(request,"all_tasks_flat.html",{'tasks':tasks})

def view_task_projects(request,status_pk:int):
    status=Status.objects.get(pk=status_pk)
    task_projects = TaskProject.objects.filter(status=status)
    return render(request,"task_projects.html",{"task_projects":task_projects})

def view_tasks_of_project(request,task_project_pk:int,status_pk:int):    
    task_project=TaskProject.objects.get(pk=task_project_pk)
    status=Status.objects.get(pk=status_pk)
    statuses=Status.objects.all()
    tasks = Task.objects.filter(task_project=task_project).filter(status=status)
    return render(request,"tasks_of_project.html",{"task_project":task_project,"tasks":tasks,"statuses":statuses})
