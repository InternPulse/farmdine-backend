from rest_framework import serializers
from .models import Event, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for the Comment model."""
    class Meta:
        model = Comment
        fields = ['id', 'event', 'text']
        read_only_fields = ['event']


class LikeSerializer(serializers.ModelSerializer):
    """Serializer for the Like model."""
    class Meta:
        model = Like
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    """Serializer for the Event model."""
    class Meta:
        model = Event
        fields = '__all__'
