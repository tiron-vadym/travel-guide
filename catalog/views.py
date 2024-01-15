from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView

from catalog.models import User, City, Review, Route


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_users = User.objects.count()
    num_cities = City.objects.count()
    num_reviews = Review.objects.count()
    num_routes = Route.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_users": num_users,
        "num_cities": num_cities,
        "num_reviews": num_reviews,
        "num_routes": num_routes,
        "num_visits": num_visits + 1
    }
    return render(request, "catalog/index.html", context=context)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "user_list.html"
    context_object_name = "users"


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "user_detail.html"
    context_object_name = "user"


class CityListView(ListView):
    model = City
    template_name = "city_list.html"
    context_object_name = "cities"


class CityDetailView(LoginRequiredMixin, DetailView):
    model = City
    template_name = "city_detail.html"
    context_object_name = "city"


class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = "review_list.html"
    context_object_name = "reviews"


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review
    template_name = "review_detail.html"
    context_object_name = "review"


class RouteListView(LoginRequiredMixin, ListView):
    model = Route
    template_name = "route_list.html"
    context_object_name = "routes"


class RouteDetailView(LoginRequiredMixin, DetailView):
    model = Route
    template_name = "route_detail.html"
    context_object_name = "route"
