from django.contrib import admin
from .models import Order, OrderDetails

# Register your models here.
admin.site.register(OrderDetails)
admin.site.register(Order)
