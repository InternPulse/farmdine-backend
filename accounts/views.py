from rest_framework import status
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from .serializers import CustomUserSerializer, VendorProfileSerializer, RestaurantProfileSerializer
from .models import CustomUser

class VendorRegisterView(APIView):
    ''' Registers CustomUser and creates VendorProfile '''
    permission_classes = [AllowAny]

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


        return Response({
            'user': user_serializer.data,
            'vendor_profile': vendor_serializer.data
        }, status=status.HTTP_201_CREATED)



class RestaurantRegisterView(APIView):
    ''' Registers CustomUser and creates VendorProfile '''
    
    permission_classes = [AllowAny]

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
        context =  Response({
                'user': user_serializer.data,
                'restaurant_profile': restaurant_serializer.data,
            }, status=status.HTTP_201_CREATED)
        
        return context
    


class LoginView(APIView):
    ''' CustomUser Email Login View '''

    permission_classes = [AllowAny]

    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
        except KeyError:
            raise AuthenticationFailed('Email and password are required.')

        if not email or not password:
            raise AuthenticationFailed('Email and password are required.')

        user = CustomUser.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('Email Address Not Found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        
        refresh = RefreshToken.for_user(user)

        response = Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
        return response
    


class UserDetailView(APIView):
    """
    View to retrieve, update or delete a user instance.
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
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        ''' Updates Only CustomUser. Doesn't Update VendorProfile or Restaurant Profile'''
        user_instance = self.get_object()
        serializer = self.serializer_class(user_instance, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        user_instance = self.get_object()
        user_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class LogoutView(APIView):
    ''' Log CustomUser out '''
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        except TokenError as e:
            return Response({"message": "Invalid token.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
