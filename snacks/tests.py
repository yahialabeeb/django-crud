from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snack = Snack.objects.create(
            title="banana", description="1", purshaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "banana")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "banana")
        self.assertEqual(f"{self.snack.purshaser}", "tester")
        self.assertEqual(self.snack.description, "1")


    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "Rake",
                "description": "2",
                "purshaser": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        self.assertContains(response, "Rake")



    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"title": "Updated title","description":"3","purshaser":self.user.id}
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)
