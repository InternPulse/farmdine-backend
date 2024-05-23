from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import VendorVerification

# Test cases for the verification app


class VendorVerificationTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='vendor',
            password='password',
            is_vendor=True
        )
        self.client.login(username='vendor', password='password')

    def test_request_verification(self):
        url = reverse('request_verification')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_verification_status(self):
        VendorVerification.objects.create(user=self.user)
        url = reverse('get_verification_status', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
