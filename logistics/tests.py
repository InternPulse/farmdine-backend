from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from orders.models import Order

class OrderAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.order = Order.objects.create(order_id='12345', status='in_progress')

    def test_get_order_by_id(self):
        url = reverse('order-detail', kwargs={'order_id': self.order.order_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['order_id'], self.order.order_id)
        self.assertEqual(response.data['status'], self.order.status)

    def test_update_order_status(self):
        url = reverse('order-detail', kwargs={'order_id': self.order.order_id})
        data = {'status': 'done'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'done')