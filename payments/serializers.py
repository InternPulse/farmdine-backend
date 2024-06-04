from rest_framework import serializers
from .models import Payment
from cart.serializers import CartDetailSerializer

class PaymentSerializer(serializers.ModelSerializer):
    cart_id = serializers.CharField(write_only=True)
    cart = CartDetailSerializer(read_only=True)
    class Meta:
        model = Payment
        fields = ["id", "cart_id", "cart", "email", "phone_number", "address", "payment_amount"]
