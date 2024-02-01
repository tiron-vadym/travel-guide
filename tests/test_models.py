from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.models import Review, City


class ModelTests(TestCase):
    def test_city_str(self):
        city = City.objects.create(
            name="test",
            country="test",
            population="100000",
            attractions="test"
        )
        self.assertEqual(str(city), city.name)

    def test_user_str(self):
        user = get_user_model().objects.create(
            username="test",
            first_name="test_first",
            last_name="test_last"
        )
        self.assertEqual(str(user), user.username)

    def test_review_str(self):
        author = get_user_model().objects.create(
            username="test",
            first_name="test_first",
            last_name="test_last"
        )
        city = City.objects.create(
            name="test",
            country="test",
            population="100000",
            attractions="test"
        )
        review = Review.objects.create(
            rating=4,
            comment="hello",
            author=author,
            city=city
        )
        self.assertEqual(str(review), f"{review.rating} - {review.comment}")
