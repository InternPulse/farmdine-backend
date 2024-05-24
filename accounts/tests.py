from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import CustomUser, VendorProfile, RestaurantProfile
from rest_framework_simplejwt.tokens import RefreshToken


class VendorRegisterViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('vendor-register')

    def test_register_vendor(self):
        data = {
            'email': 'vendor@example.com',
            'first_name': 'Vendor',
            'last_name': 'User',
            'username': 'vendoruser',
            'password': 'vendorpassword',
            'phone_number': '1234567890',
            'business_name': 'Vendor Business',
            'vendor_address': 'Vendor Address',     
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(VendorProfile.objects.count(), 1)


class RestaurantRegisterViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('restaurant-register')

        def test_register_restaurant(self):
            data = {
                'email': 'restaurant@example.com',
                'first_name': 'Restaurant',
                'last_name': 'User',
                'username': 'restaurantuser',
                'password': 'restaurantpassword',
                'phone_number': '0987654321',
                'business_name': 'Restaurant Business',
                'restaurant_address': 'Restaurant Address',
            }   
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(CustomUser.objects.count(), 1)
            self.assertEqual(RestaurantProfile.objects.count(), 1)   


class LoginViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('login')
        self.user = CustomUser.objects.create_user(
            email='login@example.com',
            password='password123',
            username='loginuser'
        )

        def test_login(self):
            data = {
                'email': 'login@example.com',
                'password': 'password123'                
            }
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIn('access', response.data)
            self.assertIn('refresh', response.data)

class UserDetailViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email='user@example.com',
            password='password123',
            username='testuser'
        )
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.url = reverse('user-detail')

    def test_get_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)

    def test_update_user_details(self):
        data = {
            'first_name': 'UpdatedName',
            'password': 'UpdatedPassword123',
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'UpdatedName')

    def test_delete_user(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CustomUser.objects.count(), 0)        


class LogoutViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email='logout@example.com',
            password='password123',
            username='logoutuser'
        )
        self.refresh_token = RefreshToken.for_user(self.user)
        self.access_token = self.refresh_token.access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.url = reverse('logout')

    def test_logout(self):
        data = {
            'refresh_token': str(self.refresh_token)
        }
        response = self.client.post(self.url, data, format='json')
        print(response.data)  # Add this line to print the response data for debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Successfully logged out.')
