from django.urls import reverse_lazy
from django.views import generic

from mission.models import Task


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10
