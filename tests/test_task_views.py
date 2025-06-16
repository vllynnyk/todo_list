from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from django.utils.timezone import make_aware

from mission.models import Task, Tag

TASK_URL = reverse("mission:task_list")


class TaskViewTests(TestCase):

    def setUp(self) -> None:
        self.tag1 = Tag.objects.create(name="work")
        self.tag2 = Tag.objects.create(name="home")
        self.tag3 = Tag.objects.create(name="shop")
        deadline_dt = make_aware(datetime.strptime("2025-06-15T10:00", "%Y-%m-%dT%H:%M"))

        task1 = Task.objects.create(
            content="load the dishwasher",
            is_completed=False,
            deadline=deadline_dt,
        )
        task1.tags.set([self.tag1])

        task2 = Task.objects.create(
            content="clean microwave",
            is_completed=False,
        )
        task2.tags.set([self.tag2])

        task3 = Task.objects.create(
            content="vacuuming",
            is_completed=False,
        )
        task3.tags.set([self.tag2, self.tag3])

    def test_uses_correct_context(self):
        response = self.client.get(TASK_URL)
        self.assertTemplateUsed(response, "mission/task_list.html")

    def test_list_tasks(self):
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "load the dishwasher")
        self.assertContains(response, "clean microwave")
        self.assertContains(response, "vacuuming")

    def test_create_task(self):
        tag = Tag.objects.create(name="job")
        response = self.client.post(
            reverse("mission:task_create"),
            {"content": "Buy bananas", "is_completed": False, "tags": [tag.id]},
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, TASK_URL)
        exists = Task.objects.filter(content="Buy bananas").exists()
        self.assertTrue(exists)

    def test_update_task(self):
        task = Task.objects.get(content="load the dishwasher")
        response = self.client.post(
            reverse("mission:task_update", kwargs={"pk": task.pk}),
            {
                "content": "load the washing machine",
                "is_completed": task.is_completed,
                "tags": [self.tag1.id, self.tag2.id],
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, TASK_URL)
        exists = Task.objects.filter(content="load the washing machine").exists()
        self.assertTrue(exists)

    def test_delete_task(self):
        task = Task.objects.get(content="vacuuming")
        response = self.client.post(
            reverse("mission:task_delete", kwargs={"pk": task.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, TASK_URL)
        exists = Task.objects.filter(content="vacuuming").exists()
        self.assertFalse(exists)
