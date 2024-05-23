from rest_framework import status
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomUserSerializer, VendorProfileSerializer, RestaurantProfileSerializer
from .models import CustomUser, VendorProfile, RestaurantProfile

class VendorRegisterView(APIView):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        # Make a mutable copy of request.data
        data = request.data.copy()
        print('data=====', data)

        # Extract user data
        user_data = {
            'email': str(data.pop('email',)),
            'full_name': str(data.pop('full_name', None)),
            'password': str(data.pop('password', None)),
            'phone_number': str(data.pop('phone_number', ''))
        }

                # Debugging: Print extracted user data
        print("Extracted user data:", user_data)

        # Validate and save user
        user_serializer = CustomUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save(is_vendor=True)

        # Prepare vendor profile data
        vendor_data = {
            'business_name': str(data.pop('business_name', None)),
            'vendor_address': str(data.pop('vendor_address', None)),
            'vendor': user.id
        }

            # Debugging: Print extracted user data
        print("Extracted user data:", vendor_data)

        # Validate and save vendor profile
        vendor_serializer = VendorProfileSerializer(data=vendor_data)
        vendor_serializer.is_valid(raise_exception=True)
        vendor_serializer.save()

        return Response({
            'user': user_serializer.data,
            'vendor_profile': vendor_serializer.data
        }, status=status.HTTP_201_CREATED)


class RestaurantRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RestaurantProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)