from rest_framework import serializers
from .models import VendorVerification


class VendorVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorVerification
        fields = ['user', 'is_verified', 'request_date', 'verification_date']
