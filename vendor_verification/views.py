from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import VendorVerification
from .serializers import VendorVerificationSerializer
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

CustomUser = get_user_model()


@swagger_auto_schema(method='post', query_serializer=VendorVerificationSerializer, 
                     responses={200: 'OK'})
@api_view(['POST'])
def request_verification(request):
    """
        Request vendor verification

        Checks if verification request exists. Creates verification request if not 
        and ensures that only Vendor users gets verified
    """

    user = request.user
    # check if user is a vendor
    if not CustomUser.objects.filter(id=user.id, is_vendor=True).exists():
        response_data = {
            'success': False,
            'status': 403,
            'error': 'Forbidden',
            'message': 'A Restaurant user is not allowed to verify'
        }
        return Response(response_data, status=status.HTTP_403_FORBIDDEN)
    
    if VendorVerification.objects.filter(user=user).exists():
        response_data = {
            'success': False,
            'status': 400,
            'error': 'Bad request',
            'message': 'Verification request already exists.'
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    
    # create a vendor verification request 
    verification = VendorVerification.objects.create(user=user)
    serializer = VendorVerificationSerializer(verification)
    response_data = {
        'success': True,
        'status': 201,
        'error': None,
        'message': 'Verification request has been created', 
        'data': serializer.data       
    }
    return Response(response_data, status=status.HTTP_201_CREATED)



@swagger_auto_schema(method='get', query_serializer=VendorVerificationSerializer, 
                     responses={200: VendorVerificationSerializer})
@api_view(['GET'])
def get_verification_status(request, user_id):
    """
        GET verification status

        Retrieves the status of Vendor verification request
    """
    try:
        verification = VendorVerification.objects.get(user_id=user_id)
    except VendorVerification.DoesNotExist:
        response_data = {
            'success': False,
            'status': 404,
            'error': 'Not found',
            'message': 'Verification status not found.',     
        }
        return Response(response_data,status=status.HTTP_404_NOT_FOUND)
    
    serializer = VendorVerificationSerializer(verification)
    if verification.is_verified:
        response_data = {
            'success': True,
            'status': 200,
            'error': None,
            'message': 'Vendor user is verified!', 
            'data': serializer.data         
        }
    else:
        response_data = {
            'success': True,
            'status': 200,
            'error': None,
            'message': 'Vendor user is not verified!', 
            'data': serializer.data         
        }
    return Response(response_data, status=status.HTTP_200_OK)
