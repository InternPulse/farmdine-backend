from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .serializers import Payment

# Create your tests here.
class MakePaymentTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    # Valid make payment data
    def test_make_payment_success(self):
        valid_data = {
            'cart_id': 'ea8aff82-f08b-4ef0-9a88-5756b12e4684',
            'email': 'johndoe@example.com',
            'phone_number': '08078828296',
            'address': 'adekunle str',
            'payment_amount': 20500,
        }
        response = self.client.post('/api/payments/make-payment/', valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the expected reference is returned
        paystack_res = response.data["data"]
        db_query = Payment.objects.get(id=paystack_res['reference'])
        self.assertTrue("reference" in paystack_res)
        self.assertEqual(paystack_res['reference'], str(db_query.id))

    # Invalid make payment data (validate email field)
    def test_make_payment_invalid_email(self):
        invalid_data = {
            'cart_id': 'ea8aff82-f08b-4ef0-9a88-5756b12e4684',
            'email': 'johndoe.example.com',
            'phone_number': '08078828296',
            'address': 'adekunle str',
            'payment_amount': 5000,
        }
        response = self.client.post('/api/payments/make-payment/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check if the expected error message is returned
        expected_error = {
            "email": ["Enter a valid email address."],
        }
        self.assertEqual(response.data, expected_error)

    # Invalid make payment data (missing required field 'cart_items_id, and payment_amount')
    def test_make_payment_required_data(self):
        invalid_data = {
            'email': 'johndoe@example.com',
            'phone_number': '08078828296',
            'address': 'adekunle str'
        }
        response = self.client.post('/api/payments/make-payment/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check if the expected error message is returned
        expected_error = {
            "cart_id": ["This field is required."],
            "payment_amount": ["This field is required."]
        }
        self.assertEqual(response.data, expected_error)


class VerifyPaymentTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        valid_data = {
            'cart_id': 'ea8aff82-f08b-4ef0-9a88-5756b12e4684',
            'email': 'dave@example.com',
            'phone_number': '08078828296',
            'address': 'adekunle str',
            'payment_amount': 20500,
        }
        response = self.client.post('/api/payments/make-payment/', valid_data, format='json')
        print(response.json())
        self.paystack_ref = response.json()['data']['reference']

    # Validate payment data
    def test_validate_payment(self):
        response = self.client.get(f'/api/payments/verify-payment/{self.paystack_ref}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the transaction status is True
        self.assertTrue("status" in response.data)
        self.assertEqual(response.data["status"], "success")

    # valid but unsuccessful payment reference data
    def test_unsuccssful_payment_ref(self):
        response = self.client.get(f'/api/payments/verify-payment/{self.paystack_ref}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_402_PAYMENT_REQUIRED)
        # Check if the transaction status is True
        self.assertTrue("status" in response.data)
        self.assertEqual(response.data["status"], "abandoned")

    # Invalid payment reference data
    def test_invalid_payment_ref(self):
        reference = 'ea8aff82-f08b-4ef0-9a88-5756b12e4684'
        response = self.client.get(f'/api/payments/verify-payment/{reference}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check if the expected error message is returned
        expected_error = 'Transaction reference not found'
        self.assertEqual(response.json()['message'], expected_error)

    # Missing payment reference data
    def test_missing_payment_ref(self):
        response = self.client.get('/api/payments/verify-payment/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
