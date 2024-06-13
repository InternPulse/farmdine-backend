"""
Title: Comment API Endpoints for Adding Comments and Likes

Description:
Defines API endpoints for adding comments and likes to comments. 
Utilizes Django REST Framework's @api_view decorator, serializers for validation, and Swagger auto-schema for documentation.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='post', request_body=CommentSerializer, 
                     responses={200: 'OK', 400: 'Bad Request'})
@api_view(['POST'])
def add_comment(request):
    """
    Add Comment Endpoint

    Handles POST requests to add a comment. Validates input data using CommentSerializer
    and saves the comment with the requesting user. Returns appropriate response with 
    serialized data on success or errors on validation failure.
    """
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@swagger_auto_schema(method='post', request_body=CommentSerializer, 
                     responses={200: 'OK', 400: 'Bad Request'})
@api_view(['POST'])
def add_like_to_comment(request, comment_id):
    """
    Add Like to Comment Endpoint

    Handles POST requests to add a like to a specific comment identified by `comment_id`.
    Creates a new like associated with the comment and the requesting user.
    Returns a success message if the like is added successfully.
    """
    comment = Comment.objects.get(pk=comment_id)
    # Assuming you have authentication implemented to get the user making the request
    like = comment.likes.create(user=request.user)
    like.save()
    return Response({'message': 'Like added successfully'}, status=201)
