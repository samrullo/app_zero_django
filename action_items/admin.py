from django.contrib import admin
from .models import TaskProject,Task,Comment,Status
# Register your models here.

class StatusAdmin(admin.ModelAdmin):
    pass
class TaskAdmin(admin.ModelAdmin):
    pass

class TaskProjectAdmin(admin.ModelAdmin):
    pass

class TaskCommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Status,StatusAdmin)
admin.site.register(TaskProject,TaskProjectAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(Comment,TaskCommentAdmin)
