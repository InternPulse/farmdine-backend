"""
Comments App Tests

Defines the test cases for the Comments app.
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Comment

class CommentAPITest(TestCase):
    """
    Comment API Tests

    Test cases for the Comment API endpoints.

    Attributes:
        CommentAPITest (class): Test case class for the Comment API endpoints.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.

        This method is called before the execution of any individual test method.
        """
        pass

    def test_add_comment(self):
        """
        Test adding a comment.

        Validates the POST request to add a new comment.
        """
        pass

    def test_add_like_to_comment(self):
        """
        Test adding a like to a comment.

        Validates the POST request to add a like to an existing comment.
        """
        pass

