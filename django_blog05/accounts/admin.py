from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomModel
from .forms import CustomUserChange, CustomUserCreation
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserChange
    model = CustomModel
    list_display = ['username', 'first_name', 'last_name', 'email', 'age', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )


admin.site.register(CustomModel, CustomUserAdmin)
