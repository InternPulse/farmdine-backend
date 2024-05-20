from django.db import models

class Product(models.Model):
    """Model representing a product."""
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

class Event(models.Model):
    """Model representing an event."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    
