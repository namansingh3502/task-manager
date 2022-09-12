from django.contrib import admin

from task_manager_app.models import Task


# Register your models here.


@admin.register(Task)
class ChannelAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Task ', {
            'fields': ('user', 'title', 'completed')
        }),
    )
