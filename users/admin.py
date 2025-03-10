from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ("id", "email", "username", "is_active", "is_verified", "created_at")  # Ko‘rinadigan maydonlar
    search_fields = ("email", "username", "first_name", "last_name")  # Qidirish maydonlari
    list_filter = ("is_active", "is_verified", "is_staff")  # Filtrlar
    ordering = ("-created_at",)  # Default tartib (oxirgi qo‘shilganlar birinchi)
    readonly_fields = ("created_at", "updated_at")  # Faqat ko‘rish mumkin bo‘lgan maydonlar

    fieldsets = (
        ("Basic Info", {"fields": ("email", "username", "first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_verified", "is_staff", "is_superuser")}),
        ("Important Dates", {"fields": ("created_at", "updated_at")}),
    )

    add_fieldsets = (
        (
            "Create New User",
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )

admin.site.register(User, UserAdmin)


# from django.contrib import admin
# from .models import User
#
# admin.site.register(User)
