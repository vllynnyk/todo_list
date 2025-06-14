from django.urls import reverse_lazy
from django.views import generic

from mission.models import Task


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("mission:task_list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("mission:task_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("mission:task_list")
