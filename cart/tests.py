from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import CustomUser
from products.models import Product
from cart.models import Cart, CartItems
import uuid

class CartManagementTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )
        self.product = Product.objects.create(
            name='Test Product',
            price=10.00,
            description='Test Description',
            stock=100
        )
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItems.objects.create(cart=self.cart, product=self.product, quantity=3, item_total_price=30.00)

    def test_add_to_cart(self):
        url = reverse('add to cart', kwargs={'user_id': str(self.user.id)})
        data = {'product_id': self.product.id, 'quantity': 2}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Item added to cart')
        self.cart_item.refresh_from_db()
        self.assertEqual(self.cart_item.quantity, 2)
        self.assertEqual(self.cart_item.item_total_price, 20.00)

    def test_remove_from_cart(self):
        url = reverse('remove from cart', kwargs={'user_id': str(self.user.id)})
        data = {'product_id': self.product.id}
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Item removed from cart')
        self.assertEqual(CartItems.objects.count(), 0)

    def test_update_cart_item_quantity(self):
        url = reverse('update cart item quantity', kwargs={'user_id': str(self.user.id)})
        data = {'product_id': self.product.id, 'quantity': 5}
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Cart item quantity updated')
        self.cart_item.refresh_from_db()
        self.assertEqual(self.cart_item.quantity, 5)

    def test_clear_cart(self):
        url = reverse('clear cart', kwargs={'user_id': str(self.user.id)})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Cart cleared')
        self.assertEqual(CartItems.objects.count(), 0)

    def test_view_cart(self):
        url = reverse('view cart', kwargs={'user_id': str(self.user.id)})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['items']), 1)
        self.assertEqual(response.data['total_price'], 30.00)
