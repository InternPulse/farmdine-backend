"""
Title: Like API Endpoint for Adding Likes to Comments

Description:
Defines an API endpoint for adding likes to comments. 
Utilizes Django REST Framework's @api_view decorator, serializers for validation, and Swagger auto-schema for documentation.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='post', request_body=LikeSerializer, 
                     responses={200: 'OK', 400: 'Bad Request'})
@api_view(['POST'])
def add_like(request):
    def add_like(request):
    """
    Title: Add Like Endpoint
    
    Description:
    Handles POST requests to add a like to a comment. 
    Validates input data using LikeSerializer and saves the like with the requesting user. 
    Returns appropriate response with serialized data on success or errors on validation failure.
    """
    serializer = LikeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
