from django import forms

from mission.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(
            attrs={'type': 'datetime-local'}
        ),
        required=False
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        exclude = ['created_date']

