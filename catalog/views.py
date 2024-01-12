from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import User, City, Review, Route


def index(request: HttpRequest) -> HttpResponse:
    num_users = User.objects.count()
    num_cities = City.objects.count()
    num_reviews = Review.objects.count()
    num_routes = Route.objects.count()

    context = {
        "num_users": num_users,
        "num_cities": num_cities,
        "num_reviews": num_reviews,
        "num_routes": num_routes,
    }
    return render(request, "catalog/index.html", context=context)
