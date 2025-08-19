from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_superuser', 'is_active')
    list_filter = ('email', 'is_superuser', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (
            'Authentication', {
            'fields': ['email', 'password']
        }
        ),
        (
            'Permissions', {
            'fields': ['is_active', 'is_staff', 'is_superuser']
        }
        ),
        (
            'Group Permissions', {
            'fields': [
                'groups', 'user_permissions'
            ]
        }
        )
    )

    add_fieldsets = (
        (
            'Authentication', {
            'fields': [
                'email', 'password1', 'password2'
            ]
        }
        ),
        (
            'Permissions', {
            'fields': [
                'is_active', 'is_staff', 'is_superuser'
            ]
        }
        ),
        (
            'Important Dates', {
            'fields': [
                'last_login'
            ]
        }
        )
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
