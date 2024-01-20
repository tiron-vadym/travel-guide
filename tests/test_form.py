from django.test import TestCase

from catalog.forms import (
    UserCreationForm,
    UserSearchForm,
    CitySearchForm,
    RouteSearchForm
)


class FormsTest(TestCase):
    def test_user_creation_form(
            self
    ):
        form_data = {
            "username": "test",
            "email": "testemail@gmail.com",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "test_first",
            "last_name": "test_last",
        }
        form = UserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class UsererSearchFormTest(TestCase):
    def test_valid_search_form(self):
        form_data = {
            "username": "test_username",
        }
        form = UserSearchForm(data=form_data)

        self.assertTrue(form.is_valid())


class CityCreationFormTest(TestCase):
    def test_empty_search_form(self):
        form_data = {}
        form = UserSearchForm(data=form_data)

        self.assertTrue(form.is_valid())


class RouteCreationFormTest(TestCase):
    def test_invalid_search_form(self):
        form_data = {
            "name": "testtest123",
        }

        form = RouteSearchForm(data=form_data)

        self.assertTrue(form.is_valid())
