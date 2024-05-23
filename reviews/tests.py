from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Review
from products.models import Product

# Test cases for the reviews app


class ReviewTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user', password='password')
        self.product = Product.objects.create(
            name='Product', description='Description', price=10.0, vendor=self.user)
        self.client.login(username='user', password='password')

    def test_create_review(self):
        url = reverse('review-list')
        data = {'product': self.product.id,
                'rating': 5, 'comment': 'Great product!'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_reviews_for_product(self):
        Review.objects.create(
            user=self.user, product=self.product, rating=5, comment='Great product!')
        url = reverse('get_reviews_for_product', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_reviews_by_user(self):
        Review.objects.create(
            user=self.user, product=self.product, rating=5, comment='Great product!')
        url = reverse('get_reviews_by_user', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
