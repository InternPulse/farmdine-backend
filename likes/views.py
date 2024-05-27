from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer

@api_view(['POST'])
def add_like(request):
    serializer = LikeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
