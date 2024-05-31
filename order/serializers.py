from .models import Order, OrderDetails
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    """This class serializes order data"""
    class Meta:
        model = Order
        fields = ['id', 'user', 'order_date', 'total_amount', 'status', 'delivered']


class OrderDetailsSerializer(serializers.ModelSerializer):
    """This class serializes order details"""
    class Meta:
        model = OrderDetails
        fields = ['id', 'orderID', 'productID', 'quantity', 'price']