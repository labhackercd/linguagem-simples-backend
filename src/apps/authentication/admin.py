from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib import admin


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('profile',)}),
    )
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'last_login',
        'is_superuser',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
    )
    raw_id_fields = ('groups', 'user_permissions')


admin.site.register(CustomUser, CustomUserAdmin)
