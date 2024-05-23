from rest_framework import serializers
from .models import VendorVerification


# Serializer to convert VendorVerification model instances to JSON format
class VendorVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorVerification
        fields = ['id', 'user', 'is_verified', 'requested_at']
