from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django import forms

from catalog.models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = BaseUserCreationForm.Meta.fields + (
            "username",
            "email",
            "first_name",
            "last_name"
        )


class UserSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


class CitySearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by model"}),
    )


class RouteSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )
