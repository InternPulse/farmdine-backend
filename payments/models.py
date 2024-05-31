from django.db import models
from uuid import uuid4
from cart.models import CartItems

# Create your models here.
class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    cart_items = models.ForeignKey(CartItems, related_name='cart_list', on_delete=models.CASCADE)
    email = models.EmailField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    verified = models.BooleanField(default=False)
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-payment_date',]

    def __str__(self) -> str:
        return f"{self.id} - {self.email} - {self.payment_amount} - {self.verified}"
