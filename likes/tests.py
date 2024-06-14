"""
Likes App Tests

Defines the test cases for the Likes app.
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Like
from comments.models import Comment, CommentLike  
from django.contrib.auth import get_user_model 

CustomUser = get_user_model()


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
        cls.user = CustomUser.objects.create_user(username='testuser', password='testpassword')  # Use custom user model
        cls.comment = Comment.objects.create(user=cls.user, content='This is a test comment')  # Added comment creation

    def setUp(self):
        """
        Set up the client for each test case.
        """
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

    def test_add_like(self):
        """
        Test adding a like to a comment.
        """
        url = reverse('add_like_to_comment', args=[self.__class__.comment.id])  # Use reverse to generate URL
        response = self.client.post(url, format='json')
        print(f"Response data: {response.data}") 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Like added successfully')