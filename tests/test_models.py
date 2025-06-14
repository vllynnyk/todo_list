from django.test import TestCase

from mission.models import Task


class TaskTest(TestCase):

    def test_task_created(self):
        task = Task.objects.create(
            content="load the dishwasher",
            is_completed=False,
        )
        self.assertEqual(task.content, "load the dishwasher")
        self.assertFalse(task.is_completed)
        self.assertIsNotNone(task.created_date)