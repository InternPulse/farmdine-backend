"""
Likes Serializers

Defines the serializers for the Likes app.
"""

from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.
    """

    class Meta:
        model = Like
        fields = '__all__'
