from django.contrib import admin
from django.contrib.auth import UserAdmin as BaseUserAdmin
from .models import User, City, Review, Route


class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "password", "first_name", "last_name")


class CityAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    pass


class RouteAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Route, RouteAdmin)
