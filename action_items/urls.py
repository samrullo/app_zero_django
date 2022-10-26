from django.urls import path,include
from . import views

urlpatterns = [path("",views.home,name="action_item_home"),
            path("tasks/",views.view_all_tasks,name="all_tasks"),
            path("task_projects/",views.view_task_projects, name="task_projects"),
            path("task_projects/new",views.new_task_project, name="new_task_project"),
            path("task_project/<int:task_project_pk>",views.view_tasks_of_project, name="tasks_of_project"),
            path("task/<int:task_pk>",views.view_task, name="task"),
            path("task/edit/<int:task_pk>",views.edit_task,name="edit_task"),
            path("task/new/<int:task_project_pk>",views.new_task,name="new_task")
            ]