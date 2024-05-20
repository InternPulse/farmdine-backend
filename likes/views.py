# likes/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Like
from .serializers import LikeSerializer

class LikeCreate(generics.CreateAPIView):
    """API endpoint for creating a like."""
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeDelete(generics.DestroyAPIView):
    """API endpoint for deleting a like."""
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
