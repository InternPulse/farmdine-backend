from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer

@api_view(['POST'])
def add_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def add_like_to_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    # Assuming you have authentication implemented to get the user making the request
    like = comment.likes.create(user=request.user)
    like.save()
    return Response({'message': 'Like added successfully'}, status=201)
