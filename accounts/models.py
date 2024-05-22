import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    """
    This handles the creation of vendors, restaurant and superusers collectively referred to as USERS, ensuring that the necessary fields are set correctly.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email Field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    This model unifies Vendor and Restaurant models via a OnetoOne relationship. 
    It will serve as the default authentication model via AUTH_USER_MODEL in settings.py
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True) 
    last_login = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [email, full_name]

    def __str__(self):
        return f'{self.email}'
    
    class Meta:
        verbose_name_plural = 'CustomUser'
        ordering = ['-date_joined']


class VendorUser(models.Model):
    """
    Has a OnetoOne Relationship with CustomUser
    Stores unique fields of the Vendor (Farmer)
    """
    vendor = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    business_name = models.CharField(max_length=255)
    vendor_address = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.business_name


class RestaurantUser(models.Model):
    """
    Has a OnetoOne Relationship with CustomUser
    Stores unique fields of Restaurant
    """
    restaurant = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    business_name = models.CharField(max_length=255)
    restaurant_address = models.CharField(max_length=300)  

    def __str__(self) -> str:
        return self.business_name














