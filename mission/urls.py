from django.urls import path

from mission.views import TaskListView


app_name = "mission"

urlpatterns = [
    path("", TaskListView.as_view(), name="todo_list"),

]