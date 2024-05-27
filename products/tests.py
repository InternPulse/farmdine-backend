from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    """Test cases for the Product model."""

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        Product.objects.create(name='Test Product', description='Test Description', price=10.99, stock=100)

    def test_name_label(self):
        """Test the label of the 'name' field."""
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        """Test the label of the 'description' field."""
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_price_label(self):
        """Test the label of the 'price' field."""
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_stock_label(self):
        """Test the label of the 'stock' field."""
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('stock').verbose_name
        self.assertEqual(field_label, 'stock')

    def test_name_max_length(self):
        """Test the maximum length of the 'name' field."""
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)
