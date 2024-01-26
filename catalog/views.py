from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from catalog.models import User, City, Review, Route
from catalog.forms import (
    UserCreationForm,
    UserSearchForm,
    CitySearchForm,
    RouteSearchForm
)


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
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = UserSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = User.objects.all()
        form = UserSearchForm(self.request.GET)
        if form.is_valid():
            queryset = queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "catalog/user_detail.html"
    context_object_name = "user"


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    success_url = reverse_lazy("catalog:user-list")
    form_class = UserCreationForm


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("catalog:user-list")


class CityListView(ListView):
    model = City
    template_name = "city_list.html"
    context_object_name = "cities"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CityListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = CitySearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = City.objects.all()
        form = CitySearchForm(self.request.GET)
        if form.is_valid():
            queryset = queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class CityDetailView(LoginRequiredMixin, DetailView):
    model = City
    template_name = "catalog/city_detail.html"
    context_object_name = "city"


class CityCreateView(LoginRequiredMixin, CreateView):
    model = City
    fields = "__all__"
    success_url = reverse_lazy("catalog:city-list")
    template_name = "catalog/city_form.html"


class CityUpdateView(LoginRequiredMixin, UpdateView):
    model = City
    fields = "__all__"
    success_url = reverse_lazy("catalog:city-list")
    template_name = "catalog/city_form.html"


class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    fields = "__all__"
    success_url = reverse_lazy("catalog:city-list")
    template_name = "catalog/city_confirm_delete.html"


class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = "review_list.html"
    context_object_name = "reviews"
    paginate_by = 5


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review
    template_name = "catalog/review_detail.html"
    context_object_name = "review"


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = "__all__"
    success_url = reverse_lazy("catalog:review-list")
    template_name = "catalog/review_form.html"


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = "__all__"
    success_url = reverse_lazy("catalog:review-list")
    template_name = "catalog/review_form.html"


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    fields = "__all__"
    success_url = reverse_lazy("catalog:review-list")
    template_name = "catalog/review_confirm_delete.html"


class RouteListView(LoginRequiredMixin, ListView):
    model = Route
    template_name = "route_list.html"
    context_object_name = "routes"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RouteListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = RouteSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Route.objects.all()
        form = RouteSearchForm(self.request.GET)
        if form.is_valid():
            queryset = queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class RouteDetailView(LoginRequiredMixin, DetailView):
    model = Route
    template_name = "catalog/route_detail.html"
    context_object_name = "route"


class RouteCreateView(LoginRequiredMixin, CreateView):
    model = Route
    fields = "__all__"
    success_url = reverse_lazy("catalog:route-list")
    template_name = "catalog/route_form.html"


class RouteUpdateView(LoginRequiredMixin, UpdateView):
    model = Route
    fields = "__all__"
    success_url = reverse_lazy("catalog:route-list")
    template_name = "catalog/route_form.html"


class RouteDeleteView(LoginRequiredMixin, DeleteView):
    model = Route
    fields = "__all__"
    success_url = reverse_lazy("catalog:route-list")
    template_name = "catalog/route_confirm_delete.html"
