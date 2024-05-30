from rest_framework import serializers
from .models import Logistics


class LogisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logistics
        fields = ['id', 'order', 'status', 'updated_at']
