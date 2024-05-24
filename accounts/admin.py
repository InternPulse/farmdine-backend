from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, VendorProfile, RestaurantProfile

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_vendor', 'is_restaurant')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_vendor', 'is_restaurant'),
        }),
    )
    list_display = ('email', 'first_name', 'username', 'is_vendor', 'is_restaurant', 'is_superuser')
    search_fields = ('email', 'username')
    ordering = ('-date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(VendorProfile)
admin.site.register(RestaurantProfile)