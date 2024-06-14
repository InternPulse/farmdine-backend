from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Comment, CommentLike
from likes.models import Like
from .serializers import CommentSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='post', request_body=CommentSerializer, 
                     responses={200: 'OK', 400: 'Bad Request'})
@api_view(['POST'])
def add_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        response = {
            'success': True,
            'status': status.HTTP_201_CREATED,
            'error': None,
            'message': 'Successfully Added Comment',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_201_CREATED)
    response = {
        'success': False,
        'status': status.HTTP_400_BAD_REQUEST,
        'error': serializer.errors,
        'message': 'Failed to Add Comment'
    }
    return Response(response, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='post', request_body=None, 
                     responses={200: 'OK', 400: 'Bad Request'})
@api_view(['POST'])
def add_like_to_comment(request, comment_id):
    """
    Add Like to Comment Endpoint

    Handles POST requests to add a like to a specific comment identified by `comment_id`.
    Creates a new like associated with the comment and the requesting user.
    Returns a success message if the like is added successfully.
    """
    try:
        print("add_like_to_comment called")  
        comment = Comment.objects.get(pk=comment_id)
        print(f"Comment found: {comment}") 
        like = Like.objects.create(comment=comment, user=request.user)
        like.save()
        response = {
            'success': True,
            'status': status.HTTP_201_CREATED,
            'error': None,
            'message': 'Like added successfully',
            'data': {
                'comment_id': comment_id,
                'user_id': request.user.id
            }
        }
        return Response(response, status=status.HTTP_201_CREATED)
    except Comment.DoesNotExist:
        print("Comment not found") 
        response = {
            'success': False,
            'status': status.HTTP_404_NOT_FOUND,
            'error': 'Comment not found',
            'message': 'Failed to add like'
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(f"Exception: {e}")
        response = {
            'success': False,
            'status': status.HTTP_400_BAD_REQUEST,
            'error': str(e),
            'message': 'Failed to add like'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
