from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cart.models import Cart
from .services import create_order_from_cart, update_order_delivery
from cart.services import get_cart_details
from .serializers import OrderDetailsSerializer, OrderSerializer
from .models import Order, OrderDetails
from products.models import Product
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
@api_view(['POST'])
def create_order_view(request):
    """This function handles order creation"""
    try:
        cart = Cart.objects.get(user=request.user)
        order = create_order_from_cart(cart)
        return Response({
            "message": "Order created",
            "order_id": order.id,
            "status": order.status,
            }, status=status.HTTP_201_CREATED)
    except Cart.DoesNotExist:
        return Response({"error": "Cart is empty"}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(method='patch', request_body=OrderSerializer, 
                     responses={200: 'OK', 400: 'Bad Request'})
@api_view(['PATCH'])
def update_order_status(request, order_id):
    """This function updates the delivery status of an order"""
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
    
    status = request.data.get('delivered')
    if not status:
        return Response({"error": "Please provide an order status."}, status=status.HTTP_404_NOT_FOUND)
    
    update_order_delivery(order, status)
    serializer = OrderSerializer(order)
    return Response(serializer.data, 200)


@swagger_auto_schema(method='get', query_serializer=OrderSerializer, 
                     responses={200: 'OK', 404: 'Not Found'})
@api_view(['GET'])
def get_orders_by_users(request, user_id):
    """This function retrieves users order based on thmeir id"""
    try:
        orders = Order.objects.filter(user_id=user_id)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Order.DoesNotExist:
        return Response({"error": "Orders not found"}, status=status.HTTP_404_NOT_FOUND)
    

@swagger_auto_schema(method='get', query_serializer=OrderSerializer, 
                     responses={200: 'OK', 400: 'Bad Request'})
@api_view(['GET'])
def get_order_by_id(request, order_id):
    try:
        """This function retrieves single user order per order id"""
        order = Order.objects.get(id=order_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
    

@swagger_auto_schema(method='patch', request_body=OrderSerializer, 
                     responses={200: 'OK', 400: 'Bad Request'})
@api_view(['PATCH'])
def cancel_order(request, order_id):
    try:
        """This function deletes single user order per order id"""
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
    
    order.status = order.CANCELED
    order.save()
    serializer = OrderSerializer(order)
    return Response({"message": "Order canceled successfully", 'data': serializer.data}, status=status.HTTP_200_OK)
  

# @api_view(['DELETE'])
# def delete_order_item(request, order_item_id):
#     """This function deletes an item from an order usingv thme id"""
#     try:
#         order_item = OrderDetails.objects.get(id=order_item_id)
#     except OrderDetails.DoesNotExist:
#         return Response({"error": "Order item not found"}, status=status.HTTP_404_NOT_FOUND)
#     order_item.delete()
#     return Response({"message": "Order item deleted successfully"}, status=status.HTTP_200_OK)
