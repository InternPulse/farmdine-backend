from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Comment

class CommentAPITest(TestCase):
    """Test cases for the Comment API endpoints."""

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        pass

    def test_add_comment(self):
        """Test adding a comment."""
        pass

    def test_add_like_to_comment(self):
        """Test adding a like to a comment."""
        pass

