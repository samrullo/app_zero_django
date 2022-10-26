from django.shortcuts import render,redirect,reverse
from .models import Task,TaskProject,Comment,Status
from .forms import CommentForm,TaskProjectForm,TaskForm

# Create your views here.
def home(request):    
    return render(request,"action_items_home.html")

def view_all_tasks(request):
    tasks=Task.objects.all()
    return render(request,"all_tasks_flat.html",{'tasks':tasks})

def view_task_projects(request):
    task_projects = TaskProject.objects.all()
    return render(request,"task_projects.html",{"task_projects":task_projects})

def view_tasks_of_project(request,task_project_pk:int):
    task_project=TaskProject.objects.get(pk=task_project_pk)
    tasks = Task.objects.filter(task_project=task_project)
    return render(request,"tasks_of_project.html",{"task_project":task_project,"tasks":tasks})

def view_task(request,task_pk:int):
    task = Task.objects.get(pk=task_pk)
    form = CommentForm()
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=Comment(comment=form.cleaned_data["comment"],task=task)
            comment.save()
    comments = Comment.objects.filter(task=task)
    return render(request,"task.html",{"task":task,"form":form,"comments":comments})


def edit_task(request,task_pk:int):
    task=Task.objects.get(pk=task_pk)    
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            status=Status.objects.get(pk=form.cleaned_data["status"])
            task.name=form.cleaned_data["name"]
            task.description=form.cleaned_data["description"]
            task.status=status
            task.deadline=form.cleaned_data["deadline"]
            task.progress=form.cleaned_data["progress"]
            task.save()
            return redirect(reverse('task',args=[task.pk]))
    
    form=TaskForm({"name":task.name,
    "description":task.description,
    "status":task.status.pk,
    "deadline":task.deadline,
    "progress":task.progress})
    form.fields["status"].widget.choices=[(status.pk,status.longname) for status in Status.objects.all()]
    return render(request,"edit_task.html",{"task":task,"form":form})

def new_task_project(request):
    form=TaskProjectForm()
    if request.method=='POST':
        form=TaskProjectForm(request.POST)
        if form.is_valid():
            status=Status.objects.get(pk=form.cleaned_data["status"])
            task_project=TaskProject(client=form.cleaned_data["client"],
                                    project_name=form.cleaned_data["project_name"],
                                    status=status,
                                    deadline=form.cleaned_data["deadline"],
                                    progress=form.cleaned_data["progress"])
            task_project.save()
            return redirect(reverse('task_projects'))
    form.fields["status"].widget.choices = [(status.pk,status.longname) for status in Status.objects.all()]
    return render(request,'new_item.html',{"title":"New Task Project","form":form})

def new_task(request,task_project_pk:int):
    task_project=TaskProject.objects.get(pk=task_project_pk)
    form=TaskForm()
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            status=Status.objects.get(pk=form.cleaned_data["status"])
            task=Task(name=form.cleaned_data["name"],
            description=form.cleaned_data["description"],
            status=status,
            deadline=form.cleaned_data["deadline"],
            progress=form.cleaned_data["progress"],
            task_project=task_project
            )
            task.save()
            return redirect(reverse('task',args=[task.pk]))
    form.fields["status"].widget.choices = [(status.pk,status.longname) for status in Status.objects.all()]
    return render(request,"new_item.html",{"title":f"New task for project {task_project}","form":form})