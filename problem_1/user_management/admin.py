from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AuthUser

class CustomUserAdmin(UserAdmin):
    model = AuthUser
    list_display = ['email', 'username', 'role', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom Fields', {'fields': ('uuid', 'role')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_superuser', 'role'),
        }),
    )
    search_fields = ['email', 'username']
    ordering = ['email']

admin.site.register(AuthUser, CustomUserAdmin)
