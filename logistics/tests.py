from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from order.models import Order
from logistics.models import Logistics
from accounts.models import CustomUser
import uuid

class LogisticsTests(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.order = Order.objects.create(user=self.user, total_amount=100)
        self.logistics = Logistics.objects.create(order=self.order, status=Logistics.PENDING)

    def test_get_logistics_details(self):
        url = reverse('get_logistics_details', args=[self.order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data['order']), str(self.order.id))

    def test_update_logistics_status(self):
        url = reverse('update_logistics_status', args=[self.order.id])
        data = {'status': Logistics.IN_TRANSIT}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.logistics.refresh_from_db()
        self.assertEqual(self.logistics.status, Logistics.IN_TRANSIT)

    def test_get_logistics_details_not_found(self):
        url = reverse('get_logistics_details', args=[uuid.uuid4()])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_logistics_status_invalid_status(self):
        url = reverse('update_logistics_status', args=[self.order.id])
        data = {'status': 'InvalidStatus'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
