"""This module handles the view logic for cart management"""
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import Cart
from .services import add_to_cart, remove_from_cart, update_cart_item_quantity, clear_cart, get_cart_details
from products.models import Product
from rest_framework.permissions import AllowAny
from .log import logger


# Create your views here.
@permission_classes([AllowAny])
@api_view(['POST'])
def add_to_cart_view(request, user_id):
    """
        Add to Cart

        This view logic handles adding product to cart
    """

    try:
        product = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        cart_detail = add_to_cart(user_id, product, quantity)
        response_data = {
            'success': True,
            'status': 200,
            'error': None,
            'message': 'Item added to cart.',
            'data': cart_detail,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_400_BAD_REQUEST)
    except ValueError as e:
        return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

@permission_classes([AllowAny])
@api_view(['DELETE'])
def remove_from_cart_view(request, user_id):
    """
        Remove items from cart

        This view function handles removing items from the cart
    """
    try:
        product = request.data.get('product_id')

        cart_detail = remove_from_cart(user_id, product)
        response_data = {
            'success': True,
            'status': 200,
            'error': None,
            'message': 'Item removed to cart.',
            'data': cart_detail,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"Error removing item from cart: {str(e)}")
        return Response({"error": "An error occurred while removing the item from the cart"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@permission_classes([AllowAny])
@api_view(['PUT'])
def update_cart_item_quantity_view(request, user_id):
    """
        Update cart 

        This endpoint handles updating the product quantity on the cart
    """

    try: 
        product = request.data.get('product_id')
        quantity = request.data.get('quantity')

        quantity = int(quantity)
        cart_detail = update_cart_item_quantity(user_id, product, quantity)
        response_data = {
            'success': True,
            'status': 200,
            'error': None,
            'message': 'Cart item quantity updated.',
            'data': cart_detail,
        }
        return Response(response_data, status=status.HTTP_200_OK)

    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_400_BAD_REQUEST)
    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    

@permission_classes([AllowAny])
@api_view(['DELETE'])
def clear_cart_view(request, user_id):
    """
        Clears cart

        This function clears the cart once an order is placed
    """
    try:
        clear_cart(user_id)
        response_data = {
            'success': True,
            'status': 200,
            'error': None,
            'message': 'Cart cleared',
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)


@permission_classes([AllowAny])
@api_view(['GET'])
def view_cart(request, user_id):
    """
        GET cart

        Endpoint to retrieve cart details
    """
    try:
        cart_details = get_cart_details(user_id)
        response_data = {
            'success': True,
            'status': 200,
            'error': None,
            'message': 'Cart item quantity updated.',
            'data': cart_details,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)
