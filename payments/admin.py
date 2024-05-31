from django.contrib import admin
from .models import Payment

# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "cart_items", "email", "payment_amount", "verified")
    list_filter = ("verified", "payment_date",)
