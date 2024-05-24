import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
    

class CustomUser(AbstractUser):
    """
    This model unifies Vendor and Restaurant models via a OnetoOne relationship. 
    It will serve as the default authentication model via AUTH_USER_MODEL in settings.py
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_vendor = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    'other common fields'

    def __str__(self):
        return f'{self.email}'
    
    class Meta:
        verbose_name_plural = 'CustomUser'
        ordering = ['-date_joined']


class VendorProfile(models.Model):
    """
    Has a OnetoOne Relationship with CustomUser
    Stores unique fields of the Vendor (Farmer)
    pk same with CustomUser id
    """
    vendor = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, blank=True)
    business_name = models.CharField(max_length=255)
    vendor_address = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.vendor.email


class RestaurantProfile(models.Model):
    """
    Has a OnetoOne Relationship with CustomUser
    Stores unique fields of Restaurant
    pk same with CustomUser id
    """
    restaurant = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, blank=True)
    business_name = models.CharField(max_length=255)
    restaurant_address = models.CharField(max_length=300)  

    def __str__(self) -> str:
        return self.restaurant.email














