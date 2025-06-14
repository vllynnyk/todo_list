from django.test import TestCase

from mission.forms import TaskForm
from mission.models import Tag


class TaskFormTests(TestCase):
    def test_task_form_with_deadline(self):
        tag = Tag.objects.create(name="work")

        form_data = {
            "content": "load the dishwasher",
            "is_completed": False,
            "tags": [tag.id],
            "deadline": "2025-06-15T10:00",
        }

        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid(), msg=form.errors)

        task = form.save()
        self.assertEqual(task.content, form_data["content"])
        self.assertFalse(task.is_completed)
        self.assertEqual(
            task.deadline.replace(tzinfo=None).isoformat(timespec="minutes"),
            "2025-06-15T10:00"
        )
        self.assertCountEqual(list(task.tags.all()), [tag])
