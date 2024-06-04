from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import VendorVerification
from .serializers import VendorVerificationSerializer
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

CustomUser = get_user_model()


@swagger_auto_schema(method='post', query_serializer=VendorVerificationSerializer, 
                     responses={200: 'OK', 400: 'Bad Request'})
@api_view(['POST'])
def request_verification(request):
    user = request.user
    if VendorVerification.objects.filter(user=user).exists():
        return Response(
            {"detail": "Verification request already exists."},
            status=status.HTTP_400_BAD_REQUEST)
    verification = VendorVerification.objects.create(user=user)
    serializer = VendorVerificationSerializer(verification)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@swagger_auto_schema(method='get', query_serializer=VendorVerificationSerializer, 
                     responses={200: VendorVerificationSerializer, 400: 'Bad Request'})
@api_view(['GET'])
def get_verification_status(request, user_id):
    try:
        verification = VendorVerification.objects.get(user_id=user_id)
    except VendorVerification.DoesNotExist:
        return Response(
            {"detail": "Verification status not found."},
            status=status.HTTP_404_NOT_FOUND)
    serializer = VendorVerificationSerializer(verification)
    return Response(serializer.data, status=status.HTTP_200_OK)
