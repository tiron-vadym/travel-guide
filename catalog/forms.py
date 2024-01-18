from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

from catalog.models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = BaseUserCreationForm.Meta.fields + (
            "username",
            "email",
            "password",
            "first_name",
            "last_name"
        )
