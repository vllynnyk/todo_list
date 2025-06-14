from django.test import TestCase

from mission.models import Task, Tag


class TaskTest(TestCase):

    def test_task_created(self):
        task = Task.objects.create(
            content="load the dishwasher",
            is_completed=False,
        )
        self.assertEqual(task.content, "load the dishwasher")
        self.assertFalse(task.is_completed)
        self.assertIsNotNone(task.created_date)

    def test_task_str(self):
        task = Task.objects.create(
            content="load the dishwasher",
            is_completed=False,
        )
        self.assertEqual(str(task),
                         f"{task.content} - {task.created_date} - {task.is_completed}")

    def test_task_ordering_by_is_completed(self):
        Task.objects.create(
            content="load the dishwasher",
            is_completed=False,
        )
        Task.objects.create(
            content="clean microwave",
            is_completed=True
        )
        Task.objects.create(
            content="vacuuming",
            is_completed=False
        )
        all_tasks = Task.objects.all()
        self.assertEqual(all_tasks[0].content, "load the dishwasher")
        self.assertEqual(all_tasks[1].content, "vacuuming")


class TagTest(TestCase):

    def test_tag_str(self):
        tag = Tag.objects.create(
            name="home",
        )
        self.assertEqual(str(tag),
                         f"{tag.name}")
