from django.db import models
from order.models import Order
import uuid


class Logistics(models.Model):
    PENDING = 'Pending'
    IN_TRANSIT = 'In Transit'
    DELIVERED = 'Delivered'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_TRANSIT, 'In Transit'),
        (DELIVERED, 'Delivered'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='logistics')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.order.id} - {self.status}'

