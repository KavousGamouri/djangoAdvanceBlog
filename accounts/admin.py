from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_superuser']
    list_filter = ['email', 'username', 'is_superuser']
    search_fields = ['email', 'username']

    fieldsets = (
        ('Authentication', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ("is_superuser", "is_active", "is_staff")}),
        ('Group permissions', {'fields': ("groups", "user_permissions")}),
        ('Important date', {'fields': ("last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "is_superuser"
            )},
         ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
