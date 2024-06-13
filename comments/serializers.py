"""
Comments Serializers

Defines the serializers for the Comments app.
"""

from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for serializing and deserializing Comment model instances.

    Attributes:
        Meta (class): Inner class defining the metadata for the serializer.
            - model (Model): Specifies the model to be serialized (Comment).
            - fields (list): List of fields to include in the serialized output.
    """
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']
