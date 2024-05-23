from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import VendorVerification
from .serializers import VendorVerificationSerializer

# View to handle verification requests from vendors


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def request_verification(request):
    user = request.user
    if not user.is_vendor:
        return Response(
            {'error': 'Only vendors can request verification'},
            status=status.HTTP_403_FORBIDDEN
        )

    if VendorVerification.objects.filter(user=user).exists():
        return Response(
            {'error': 'Verification already requested'},
            status=status.HTTP_400_BAD_REQUEST
        )

    VendorVerification.objects.create(user=user)
    return Response(
        {'status': 'Verification requested'},
        status=status.HTTP_201_CREATED
    )

# View to get the verification status of a vendor


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_verification_status(request, user_id):
    try:
        verification = VendorVerification.objects.get(user_id=user_id)
        serializer = VendorVerificationSerializer(verification)
        return Response(serializer.data)
    except VendorVerification.DoesNotExist:
        return Response(
            {'error': 'User not found or verification not requested'},
            status=status.HTTP_404_NOT_FOUND
        )
