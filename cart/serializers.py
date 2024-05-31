"""The module handles the serializer for Cart and Cart Items"""
from rest_framework import serializers
from .models import Cart, CartItems
from products.models import Product


class CartSerializer(serializers.ModelSerializer):
    """This class handles Cart Serialization"""
    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at']


class CartItemSerializers(serializers.ModelSerializer):
    """This class handles Cart Items serialization"""
    product_name = serializers.CharField(source='product.name', read_only=True)
    unit_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    class Meta:
        model = CartItems
        fields = ['id', 'cart', 'product_id','product_name', 'quantity', 'unit_price', 'item_total_price', 'added_at']


class CartDetailSerializer(serializers.Serializer):
    """Serializes cart details"""
    items = CartItemSerializers(many=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, )
