from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            username="user",
            password="testuser",
        )

    def test_user_username_listed(self):
        """
        Test that user's username is listed_display on admin page
        """
        url = reverse("admin:catalog_user_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.user.username)

    def test_user_detail_username_listed(self):
        """
        Test that user's username is on driver detail admin page
        """
        url = reverse("admin:catalog_user_change", args=[self.user.id])
        res = self.client.get(url)
        self.assertContains(res, self.user.username)
