from django.contrib import admin
from .models import TaskProject,Task,Comment
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    pass

class TaskProjectAdmin(admin.ModelAdmin):
    pass

class TaskCommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(TaskProject,TaskProjectAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(Comment,TaskCommentAdmin)
