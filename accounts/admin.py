from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, VendorProfile, RestaurantProfile

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_vendor', 'is_restaurant')}),
        ('Personal info', {'fields': ('full_name', 'phone_number')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_vendor', 'is_restaurant'),
        }),
    )
    list_display = ('email', 'is_staff', 'is_active', 'is_vendor', 'is_restaurant')
    search_fields = ('email', 'full_name')
    ordering = ('date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(VendorProfile)
admin.site.register(RestaurantProfile)