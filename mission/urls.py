from django.urls import path

from mission.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView
)


app_name = "mission"

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path(
        "create/",
        TaskCreateView.as_view(),
        name="task_create"
    ),
    path(
        "<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task_update"
    ),
    path(
        "<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task_delete"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag_list"
    ),
]
