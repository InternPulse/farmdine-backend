from django.db import models
import uuid
from accounts.models import CustomUser
from products.models import Product


# Create your models here.
class Order(models.Model):
    """This model handles user orders"""
    CANCELED = 'Canceled'
    ORDERED = 'Ordered'
    choice = [
        (CANCELED, 'Canceled'),
        (ORDERED, 'Ordered'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='order')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=choice, default=ORDERED)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.order_no} - {self.restaurantID.business_name}'
    

class OrderDetails(models.Model):
    """This model contains all details for an order"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    productID = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.productID.name} - {self.orderID}'


