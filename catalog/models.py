from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    population = models.IntegerField()
    coordinates = models.CharField(max_length=255)
    attractions = models.TextField()


class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Route(models.Model):
    name = models.CharField(max_length=255)
    duration = models.DurationField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    points_of_interest = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
