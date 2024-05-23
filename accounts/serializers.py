from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from .models import CustomUser, VendorProfile, RestaurantProfile

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    phone_number = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'password', 'phone_number')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password'],
            phone_number=validated_data['phone_number']
        )
        return user


class VendorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = ['business_name', 'vendor_address']


class RestaurantProfileSerializer(serializers.ModelSerializer):
    restaurant = CustomUserSerializer()

    class Meta:
        model = RestaurantProfile
        fields = ('restaurant', 'business_name', 'restaurant_address')

    def create(self, validated_data):
       user_data = validated_data.pop('restaurant') 
       user = CustomUser.objects.create_user(**user_data, is_restaurant=True)
       restaurant_profile = RestaurantProfile.objects.create(restaurant=user, **validated_data)
       return restaurant_profile







