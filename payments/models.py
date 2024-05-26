from django.db import models
from uuid import uuid4

# Create your models here.
class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    # order_id = models.ForeignKey(Order, related_name='payment', on_delete=models.CASCADE)
    email = models.EmailField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    verified = models.BooleanField(default=False)
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-payment_date',)

    def __str__(self) -> str:
        return f"{self.id} - {self.email} - {self.payment_amount} - {self.verified}"
