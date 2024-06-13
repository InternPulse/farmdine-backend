"""
Comments Models

Defines the database models for the Comments app.
"""

from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Comment(models.Model):
    """
    Represents a comment made by a user.

    Attributes:
        user (ForeignKey): The user who made the comment.
        content (TextField): The content of the comment.
        created_at (DateTimeField): The date and time when the comment was created.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class CommentLike(models.Model):
    """
    Represents a like given to a comment by a user.

    Attributes:
        user (ForeignKey): The user who liked the comment.
        created_at (DateTimeField): The date and time when the like was created.
        comment (ForeignKey): The comment that was liked.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey('comments.Comment', related_name='comment_likes', on_delete=models.CASCADE)

