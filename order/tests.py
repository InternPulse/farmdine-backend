from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import CustomUser
from products.models import Product
from cart.models import Cart, CartItems
from .models import Order, OrderDetails
import uuid

class OrderManagementTestCase(TestCase):
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
       

    def test_create_order(self):
        url = reverse('create order')
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, {'user_id': self.user.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Order created')
        
        # Ensure the order is created
        order = Order.objects.filter(user=self.user).first()
        self.assertIsNotNone(order)
        
        # Ensure the order details are correct
        order_details = OrderDetails.objects.filter(orderID=order, productID=self.product).first()
        self.assertIsNotNone(order_details)
                

    def test_get_orders_by_user(self):
        self.order = Order.objects.create(user=self.user, total_amount=30.00)
        self.order_details = OrderDetails.objects.create(orderID=self.order, productID=self.product, quantity=3, price=10.00)
        url = reverse('user orders', kwargs={'user_id': self.user.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user'], self.user.id)

    def test_get_order_by_id(self):
        order = Order.objects.create(user=self.user, total_amount=30.00)
        url = reverse('order by id', kwargs={'order_id': order.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_order_id = uuid.UUID(response.data['id'])
        self.assertEqual(response_order_id, order.id)

    def test_update_order_status(self):
        order = Order.objects.create(user=self.user, total_amount=30.00)
        url = reverse('update order status', kwargs={'order_id': order.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, {'delivered': 'True'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order.refresh_from_db()
        self.assertEqual(order.delivered, True)

    def test_cancel_order(self):
        order = Order.objects.create(user=self.user, total_amount=30.00)
        url = reverse('cancel order', kwargs={'order_id': order.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order.refresh_from_db()
        self.assertEqual(order.status, Order.CANCELED)

    # def test_add_order_item(self):
    #     order = Order.objects.create(user=self.user, total_amount=30.00)
    #     url = reverse('add order item', kwargs={'order_id': order.id})
    #     data = {
    #         'order_id': order.id,
    #         'product_id': self.product.id,
    #         'quantity': 1,
    #         'price': 10.00
    #     }
    #     self.client.force_authenticate(user=self.user)
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertTrue(OrderDetails.objects.filter(orderID=self.order, productID=self.product).exists())

    # def test_update_order_item(self):
    #     order = Order.objects.create(user=self.user, total_amount=30.00)
    #     order_item = OrderDetails.objects.create(orderID=order, productID=self.product, quantity=1, price=10.00)
    #     url = reverse('update order item', kwargs={'order_item_id': order_item.id})
    #     data = {'quantity': 2, 'price': 20.00}
    #     self.client.force_authenticate(user=self.user)
    #     response = self.client.patch(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     order_item.refresh_from_db()
    #     self.assertEqual(order_item.quantity, 2)
    #     self.assertEqual(order_item.price, 20.00)

    # def test_delete_order_item(self):
    #     order = Order.objects.create(user=self.user, total_amount=30.00)
    #     order_item = OrderDetails.objects.create(orderID=order, productID=self.product, quantity=1, price=10.00)
    #     url = reverse('remove order item', kwargs={'order_item_id': order_item.id})
    #     self.client.force_authenticate(user=self.user)
    #     response = self.client.delete(url, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertFalse(OrderDetails.objects.filter(orderID=order, productID=self.product).exists())