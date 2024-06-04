"""This module handles the view logic for cart management"""
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view
from .models import Cart, CartItems
from .serializers import CartItemSerializers, CartSerializer
from .services import add_to_cart, remove_from_cart, update_cart_item_quantity, clear_cart, get_cart_details
from products.models import Product

# Create your views here.
@api_view(['POST'])
def add_to_cart_view(request, user_id):
    """This view logic handles addingv product to cart"""
    try:
        product = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        cart_detail = add_to_cart(user_id, product, quantity)
        return Response({"message": "Item added to cart", "cart":  cart_detail}, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_400_BAD_REQUEST)
    except ValueError as e:
        return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def remove_from_cart_view(request, user_id):
    """This view function handles removingv items from thme cart"""
    try:
        product = request.data.get('product_id')

        cart_detail = remove_from_cart(user_id, product)
        return Response({"message": "Item removed from cart", "cart":  cart_detail}, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def update_cart_item_quantity_view(request, user_id):
    """This view function handles updating the product quantity on the cart"""
    try: 
        product = request.data.get('product_id')
        quantity = request.data.get('quantity')

        quantity = int(quantity)
        cart_detail = update_cart_item_quantity(user_id, product, quantity)
        return Response({"message": "Cart item quantity updated", "cart":  cart_detail}, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_400_BAD_REQUEST)
    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    


@api_view(['DELETE'])
def clear_cart_view(request, user_id):
    """This function clears the cart once an order is placed"""
    try:
        clear_cart(user_id)
        return Response({"message": "Cart cleared"}, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def view_cart(request, user_id):
    """View function to view cart details"""
    try:
        cart_details = get_cart_details(user_id)
        return Response(cart_details, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)
