from django.urls import path, include
from catalog import views

from .views import (
    UserListView,
    UserDetailView,
    UserCreateView,
    UserDeleteView,
    CityListView,
    CityDetailView,
    CityCreateView,
    CityUpdateView,
    CityDeleteView,
    ReviewListView,
    ReviewDetailView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDeleteView,
    RouteListView,
    RouteDetailView,
    RouteCreateView,
    RouteUpdateView,
    RouteDeleteView, UserDeleteView,
)


urlpatterns = [
    path("", views.index, name="index"),
    path("users", UserListView.as_view(), name="user-list"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("user/create/", UserCreateView.as_view(), name="user-create"),
    path(
        "user/<int:pk>/delete/",
        UserDeleteView.as_view(),
        name="user-delete"
    ),
    path("cities/", CityListView.as_view(), name="city-list"),
    path("city/<int:pk>/", CityDetailView.as_view(), name="city-detail"),
    path(
        "city/create/",
        CityCreateView.as_view(),
        name="city-create"
    ),
    path(
        "city/<int:pk>/update/",
        CityUpdateView.as_view(),
        name="city-update"
    ),
    path(
        "city/<int:pk>/delete/",
        CityDeleteView.as_view(),
        name="city-delete"
    ),
    path("reviews/", ReviewListView.as_view(), name="review-list"),
    path(
        "review/<int:pk>/",
        ReviewDetailView.as_view(),
        name="review-detail"
    ),
    path(
        "review/create/",
        ReviewCreateView.as_view(),
        name="review-create"
    ),
    path(
        "review/<int:pk>/update/",
        ReviewUpdateView.as_view(),
        name="review-update"
    ),
    path(
        "review/<int:pk>/delete/",
        ReviewDeleteView.as_view(),
        name="review-delete"
    ),
    path("routes/", RouteListView.as_view(), name="route-list"),
    path("route/<int:pk>/", RouteDetailView.as_view(), name="route-detail"),
    path(
        "route/create/",
        RouteCreateView.as_view(),
        name="route-create"
    ),
    path(
        "route/<int:pk>/update/",
        RouteUpdateView.as_view(),
        name="route-update"
    ),
    path(
        "route/<int:pk>/delete/",
        RouteDeleteView.as_view(),
        name="route-delete"
    ),
    path("accounts/", include("django.contrib.auth.urls")),
]

app_name = "catalog"
