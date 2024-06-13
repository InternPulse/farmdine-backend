"""
Likes App Tests

Defines the test cases for the Likes app.
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Like

class LikeAPITest(TestCase):
    """
    Test cases for the Like API endpoints.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        # Setup code for creating initial data goes here.
        pass

    def setUp(self):
        """
        Set up the client for each test case.
        """
        self.client = APIClient()

    def test_add_like(self):
        """
        Test adding a like to a comment.
        """
        # Example of a test case for adding a like
        url = reverse('like-list')  # Update 'like-list' to the correct URL name
        data = {
            "user": 1,  # Assuming a user with ID 1 exists
            "comment": 1  # Assuming a comment with ID 1 exists
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
