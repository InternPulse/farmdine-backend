"""The module handles the models for Cart and Cart Items"""
from django.db import models
from accounts.models import CustomUser
import uuid
from products.models import Product


# Create your models here.
class Cart(models.Model):
    """
    This model handle users cart for product purchase
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'
    

class CartItems(models.Model):
    """
    This model contains all the items inside the cart
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cart.user.username}'
    
    class Meta: 
        verbose_name_plural = 'CartItems'