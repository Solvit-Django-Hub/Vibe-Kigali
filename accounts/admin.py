from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_business_owner', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Vibe Kigali', {'fields': ('phone_number', 'is_business_owner')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Vibe Kigali', {'fields': ('phone_number', 'is_business_owner')}),
    )
