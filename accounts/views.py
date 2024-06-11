from rest_framework import status
from django.db import transaction
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from .serializers import CustomUserSerializer, VendorProfileSerializer, RestaurantProfileSerializer, LoginSerializer, LogoutSerializer
from .models import CustomUser, VendorProfile, RestaurantProfile

class VendorRegisterView(APIView):
    """
        Register a Vendor User

        Registers CustomUser and creates VendorProfile. 
        Provide data for both models simultaneously
    """

    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=CustomUserSerializer,
        responses={
            201: VendorProfileSerializer,
        }
    )
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        # Make request.data (a QueryDict) mutable by creating a copy of it
        data = request.data.copy()

        # Extract user data
        user_data = {
            'email': data.get('email'),
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'username': data.get('username'),
            'password': data.get('password'),
            'phone_number': data.get('phone_number'),
        }

        # Validate and save CustomUser
        user_serializer = CustomUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        # set is_vendor to True and save user again
        user.is_vendor = True
        user.save()


        # Extract vendor profile data
        vendor_data = {
            'business_name': data.get('business_name'),
            'vendor_address': data.get('vendor_address'),
            'vendor': user.id,
        }

        # Validate and save vendor profile
        vendor_serializer = VendorProfileSerializer(data=vendor_data)
        vendor_serializer.is_valid(raise_exception=True)
        vendor_serializer.save()

        response = {
            'success': True,
            'status': 201,
            'error': None,
            'message': 'Successfully Registered Vendor User',
            'user': user_serializer.data,
            'vendor_profile': vendor_serializer.data
        }
        return Response(response, status=status.HTTP_201_CREATED)



class RestaurantRegisterView(APIView):
    """
        Register a Restaurant User

        Registers CustomUser and creates RestaurantProfile. 
        Provide data for both models simultaneously
    """
    
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=CustomUserSerializer,
        responses={
            201: RestaurantProfileSerializer,
        }
    )
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        # Make request.data (a QueryDict) mutable by creating a copy of it
        data = request.data.copy()
        
        # Extract user data
        user_data = {
            'email': data.get('email'),
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'username': data.get('username'),
            'password': data.get('password'),
            'phone_number': data.get('phone_number'),
        }

        # Validate and save CustomUser
        user_serializer = CustomUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        # set is_restaurant to True and save user again
        user.is_restaurant = True
        user.save()

        # Extract restaurant profile data
        restaurant_data = {
            'business_name': data.get('business_name'),
            'restaurant_address': data.get('restaurant_address'),
            'restaurant': user.id,
        }

        restaurant_serializer = RestaurantProfileSerializer(data=restaurant_data)
        restaurant_serializer.is_valid(raise_exception=True)
        restaurant_serializer.save()

        response = {
            'success': True,
            'status': 201,
            'error': None,
            'message': 'Successfully Registered Restaurant User',
            'user': user_serializer.data,
            'restaurant_profile': restaurant_serializer.data,
        }
        return Response(response, status=status.HTTP_201_CREATED)
    

class LoginView(APIView):
    """
        User Login

        User logins with their email address
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            200: 'OK',
        }
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = CustomUser.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('Email Address Not Found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        
        refresh = RefreshToken.for_user(user)

        response = {
            'success': True,
            'status': 200,
            'error': None,
            'message': 'User Login Successful',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response, status=status.HTTP_200_OK) 
    


class UserDetailView(APIView):
    """
        Endpoint to retrieve, update or delete a user instance.

        - GET: Return the details of a specific CustomUser.
        - PUT: Update a specific CustomUser.
        - DELETE: Delete a specific CustomUser.
    """
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user


    def get(self, request, *args, **kwargs):
        user_instance = self.get_object()
        serializer = self.serializer_class(user_instance)
        if user_instance.is_vendor:
            vendor_profile = VendorProfile.objects.filter(vendor=user_instance.pk).first()
            if vendor_profile:
                vendor_serializer = VendorProfileSerializer(vendor_profile)
                response_data = {
                    'success': True,
                    'status': 200,
                    'error': None,
                    'message': 'GET User and Vendor Details Successful',
                    'user': serializer.data,
                    'vendor_details': vendor_serializer.data
                }
            else:
                response_data = {
                    'success': False,
                    'status': 404,
                    'error': 'Vendor profile not found',
                    'message': 'Vendor details could not be retrieved',
                    'user': serializer.data,
                }  
                return Response(response_data, status=status.HTTP_404_NOT_FOUND)              
        
        else:
            restaurant_profile = RestaurantProfile.objects.filter(restaurant=user_instance.id).first()
            if restaurant_profile:
                restaurant_serializer = RestaurantProfileSerializer(restaurant_profile)
                response_data = {
                    'success': True,
                    'status': 200,
                    'error': None,
                    'message': 'GET User and Restaurant Details Successful',
                    'user': serializer.data,
                    'restaurant_details': restaurant_serializer.data,
                }
            else:
                response_data = {
                    'success': False,
                    'status': 404,
                    'error': 'Restaurant profile not found',
                    'message': 'Restaurant details could not be retrieved',
                    'user': serializer.data,
                }  
                return Response(response_data, status=status.HTTP_404_NOT_FOUND)              

        return Response(response_data, status=status.HTTP_200_OK)     


    @swagger_auto_schema(request_body=CustomUserSerializer, responses={200: 'OK'})
    def put(self, request, *args, **kwargs):
        ''' Updates Only User data. Doesn't Update Vendor or Restaurant data '''
        user_instance = self.get_object()
        serializer = self.serializer_class(user_instance, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            response_data = {
                    'success': True,
                    'status': 200,
                    'error': None,
                    'message': 'User Details updated successfully',
                    'user': serializer.data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    @swagger_auto_schema(request_body=CustomUserSerializer, responses={204: 'No Content'})
    def delete(self, request, *args, **kwargs):
        user_instance = self.get_object()
        user_instance.delete()
        response_data = {
                'success': True,
                'status': 204,
                'error': None,
                'message': 'User Deleted',
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)


class LogoutView(generics.GenericAPIView):
    """
        User Logout

        Logs user out by blacklisting their refresh token.
    """
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            serializer.save()
            response = {
                'success': True,
                'message': 'Logout successful. Token has been blacklisted.',
                'data': None,
                'status': status.HTTP_204_NO_CONTENT
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        
        except ValidationError as e:
            response = {
                'success': False,
                'message': 'Logout failed. Invalid token.',
                'data': {'detail': str(e)},
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            response = {
                'success': False,
                'message': 'An unexpected error occurred.',
                'data': {'detail': str(e)},
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)