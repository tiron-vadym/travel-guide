from django.urls import path, include
from catalog import views

from .views import (
    UserListView,
    UserDetailView,
    CityListView,
    CityDetailView,
    ReviewListView,
    ReviewDetailView,
    RouteListView,
    RouteDetailView,
)


urlpatterns = [
    path("", views.index, name="index"),
    path("users", UserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("cities/", CityListView.as_view(), name="city-list"),
    path("cities/<int:pk>/", CityDetailView.as_view(), name="city-detail"),
    path("reviews/", ReviewListView.as_view(), name="review-list"),
    path(
        "reviews/<int:pk>/",
        ReviewDetailView.as_view(),
        name="review-detail"
    ),
    path("routes/", RouteListView.as_view(), name="route-list"),
    path("routes/<int:pk>/", RouteDetailView.as_view(), name="route-detail"),
    path("accounts/", include("django.contrib.auth.urls")),
]

app_name = "catalog"
