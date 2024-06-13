"""
Likes Models

Defines the database models for the Likes app.
"""

from django.db import models
from django.contrib.auth import get_user_model
from comments.models import Comment

CustomUser = get_user_model()

class Like(models.Model):
    """
    Represents a 'Like' on a comment.

    Attributes:
        user (ForeignKey): The user who liked the comment.
        created_at (DateTimeField): The date and time when the like was created.
        comment (ForeignKey): The comment that was liked.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} liked {self.comment}"
