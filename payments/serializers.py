from rest_framework import serializers
from .models import Payment
from cart.serializers import CartItemSerializers


class PaymentSerializer(serializers.ModelSerializer):
    cart_items_id = serializers.CharField(write_only=True)
    cart_items = CartItemSerializers(read_only=True)
    # payment_amount = serializers.DecimalField(source="cartitems.items_total_price", max_digits=10, decimal_places=2, readonly=True)
    class Meta:
        model = Payment
        fields = ["cart_items_id", "cart_items", "email", "payment_amount"]
