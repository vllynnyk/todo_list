from django.contrib import admin

from mission.models import Tag, Task


admin.site.register(Tag)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "created_date", "is_completed")
    search_fields = ("created_date",)
    list_filter = ("is_completed",)

