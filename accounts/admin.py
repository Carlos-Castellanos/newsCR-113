from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields":("department","role")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets +(
        (None, {"fields":("department","role")}),
    )

    list_display = [
        "username", "email", "first_name", "last_name",
        "department", "role", "is_staff",
    ]

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
