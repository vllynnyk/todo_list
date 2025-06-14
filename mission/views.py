from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views import generic

from mission.forms import TaskForm
from mission.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("mission:task_list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("mission:task_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("mission:task_list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10



class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("mission:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("mission:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("mission:tag_list")


def confirm_completed_status(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        raise Http404("Task not found")
    task.is_completed = not task.is_completed
    task.save()
    return HttpResponseRedirect(reverse_lazy("mission:task_list"))
