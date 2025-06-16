from django.urls import path

from mission.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    confirm_completed_status
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
        "<int:pk>/confirm-status/",
        confirm_completed_status,
        name="confirm_status",
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag_list"
    ),
    path(
        "tag/create/",
        TagCreateView.as_view(),
        name="tag_create"
    ),
    path(
        "tag/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag_update"
    ),
    path(
        "tag/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag_delete"
    ),
]
