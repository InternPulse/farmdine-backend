from rest_framework import serializers
from .models import Payment
from cart.serializers import CartSerializer

class PaymentSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)
    payment_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = Payment
        fields = ["id", "cart", "email", "phone_number", "address", "payment_amount"]
