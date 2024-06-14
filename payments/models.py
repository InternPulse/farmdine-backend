from django.db import models
from uuid import uuid4
from cart.models import Cart

# Create your models here.
class Payment(models.Model):
    """Represent a Payment.
    
    Attributes:
        id: The payment or reference id of the initiated payment as a string.
        cart: A one-to-one relationship with the cart model.
        email: The buyer's email as a string.
        phone_number: The buyer's phone number as an string.
        address: The deliver address of the buyer as a string.
        payment_amount: The total amount for the items as a decimal.
        verified: The payment status of the items as a boolean.
        payment_date: The date and time of initiating payment for the product as a string.
    """
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    verified = models.BooleanField(default=False)
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-payment_date',]

    def __str__(self) -> str:
        return f"{self.id} - {self.email} - {self.payment_amount} - {self.verified}"
