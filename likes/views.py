from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Like 
from .serializers import LikeSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='post', request_body=LikeSerializer, 
                     responses={200: 'OK', 400: 'Bad Request'})
@api_view(['POST'])
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
        like = serializer.save(user=request.user)
        response = {
            'success': True,
            'status': 201,
            'error': None,
            'message': 'Successfully added like to the comment',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        response = {
            'success': False,
            'status': 400,
            'error': serializer.errors,
            'message': 'Failed to add like to the comment'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
