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


class TagListView(generic.ListView):
    model = Task
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("mission:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("mission:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("mission:tag_list")
