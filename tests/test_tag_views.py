from django.test import TestCase
from django.urls import reverse

from mission.models import Tag

TAG_LIST_URL = reverse("mission:tag_list")


class TagViewTests(TestCase):

    def setUp(self) -> None:
        self.tag1 = Tag.objects.create(name="work")
        self.tag2 = Tag.objects.create(name="home")

    def test_tag_list_view(self):
        response = self.client.get(TAG_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mission/tag_list.html")  # убедись, что шаблон такой
        self.assertContains(response, self.tag1.name)
        self.assertContains(response, self.tag2.name)

    def test_create_tag(self):
        response = self.client.post(
            reverse("mission:tag_create"),
            {"name": "shop"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, TAG_LIST_URL)
        exists = Tag.objects.filter(name="shop").exists()
        self.assertTrue(exists)

    def test_update_tag(self):
        response = self.client.post(
            reverse("mission:tag_update", kwargs={"pk": self.tag1.pk}),
            {"name": "office"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, TAG_LIST_URL)
        self.tag1.refresh_from_db()
        self.assertEqual(self.tag1.name, "office")

    def test_delete_tag(self):
        response = self.client.post(
            reverse("mission:tag_delete", kwargs={"pk": self.tag2.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, TAG_LIST_URL)
        exists = Tag.objects.filter(pk=self.tag2.pk).exists()
        self.assertFalse(exists)
