from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from catalog.models import Route, User
from catalog.forms import UserCreationForm, UserSearchForm

ROUTE_URL = reverse("catalog:route-list")


class PublicRouteTest(TestCase):
    def test_login_required(self):
        res = self.client.get(ROUTE_URL)
        self.assertNotEquals(res.status_code, 200)


class PrivateRouteTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_retrieve_route(self):
        author = get_user_model().objects.create(
            username="test2",
            first_name="test_first",
            last_name="test_last"
        )
        Route.objects.create(
            name="test1",
            duration=timezone.timedelta(days=5, hours=3, minutes=30),
            budget=500,
            points_of_interest="test12",
            author=author
        )
        Route.objects.create(
            name="test2",
            duration=timezone.timedelta(days=5, hours=3, minutes=30),
            budget=500,
            points_of_interest="test21",
            author=author
        )
        response = self.client.get(ROUTE_URL)
        self.assertEqual(response.status_code, 200)
        routes = Route.objects.all()
        self.assertEqual(
            list(response.context["routes"]),
            list(routes),
        )
        self.assertTemplateUsed(response, "catalog/route_list.html")

    def test_create_user(self):
        form_data = {
            "username": "test3",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "",
            "last_name": "",
        }
        response = self.client.post(
            reverse("catalog:user-create"),
            data=form_data
        )
        self.assertEqual(response.status_code, 302)

        new_user = get_user_model().objects.get(username=form_data["username"])
        self.assertIsNotNone(new_user)

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])


class SearchFeatureTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="testname",
            password="user12test"
        )
        self.client = Client()
        self.client.force_login(self.user)

        author = get_user_model().objects.create(
            username="test4",
            first_name="test_first",
            last_name="test_last"
        )
        Route.objects.create(
            name="Test Route1",
            duration=timezone.timedelta(days=5, hours=3, minutes=30),
            budget=500,
            points_of_interest="test12",
            author=author
        )
        Route.objects.create(
            name="Test Route",
            duration=timezone.timedelta(days=5, hours=3, minutes=30),
            budget=1000,
            points_of_interest="test12",
            author=author
        )
        Route.objects.create(
            name="Another Route",
            duration=timezone.timedelta(days=5, hours=3, minutes=30),
            budget=1500,
            points_of_interest="test12",
            author=author
        )

    def test_search_results(self):
        search_term = "Test Route"
        response = self.client.get(reverse("catalog:route-list"),
                                   {"name": search_term})
        self.assertEqual(response.status_code, 200)
        routes = response.context["routes"]
        self.assertEqual(len(routes), 2)

        invalid_search_term = "Invalid Route"
        response = self.client.get(reverse("catalog:route-list"),
                                   {"name": invalid_search_term})
        self.assertEqual(response.status_code, 200)
        routes = response.context["routes"]
        self.assertEqual(len(routes), 0)


class SearchTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="name123", password="password123"
        )
        self.client = Client()
        self.client.force_login(self.user)

    def test_search_user_by_username(self):
        User.objects.create(username="newuser1")
        User.objects.create(username="newuser2")

        response = self.client.get(
            reverse("catalog:user-list"), {"username": "newuser2"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context["search_form"], UserSearchForm
        )
        self.assertQuerysetEqual(
            response.context["object_list"],
            User.objects.filter(username__icontains="newuser2"),
        )


class LogoutTest(TestCase):
    def test_logout_redirect(self):

        logout_url = reverse('logout')

        response = self.client.get(logout_url)

        self.assertEqual(response.status_code, 302)
