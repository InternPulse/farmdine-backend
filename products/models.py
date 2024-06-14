from django.db import models
from accounts.models import CustomUser

class Category(models.TextChoices):
    FRUITS = 'Fruits'
    FRESH_VEG = 'Fresh Veg'
    RICE_AND_PASTA = 'Rice and Pasta'
    CEREAL = 'Cereal'
    LIVE_STOCK = 'Live Stock'


class Product(models.Model):
    """Represent a Product.
    
    Attributes:
        name: The name of the product as a string.
        category: The category of the product as a string.
        description: The description of the product as a text.
        price: The price of the product as a decimal.
        stock: The stock of the product as an integer.
        image: The image of the product as a string.
        user: A one-to-one relationship with the CustomUser model.
        date_created: The date and time of the product was created as a string.
    """
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=Category.choices)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to="farmdine/product_images/", null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
