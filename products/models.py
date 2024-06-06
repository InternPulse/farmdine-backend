from django.db import models

class Product(models.Model):
    """Model representing a product."""
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to="farmdine/product_images/", null=True, blank=True)

    def __str__(self):
        return self.name
