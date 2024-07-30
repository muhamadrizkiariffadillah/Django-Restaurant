from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, UserProfile


# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'role')
    ordering = ('-date_joined',)
    filter_horizontal: tuple = ()
    list_filter: tuple = ()
    fieldsets: tuple = ()


admin.sites.site.register(User, CustomUserAdmin)
admin.sites.site.register(UserProfile)
