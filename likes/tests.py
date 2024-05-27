from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Like

class LikeAPITest(TestCase):
    """Test cases for the Like API endpoints."""

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        pass

    def test_add_like(self):
        """Test adding a like to a comment."""
        pass


