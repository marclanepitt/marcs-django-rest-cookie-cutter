from django.contrib import admin

from .models import UserProfile


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile)
