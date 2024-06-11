from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cart.models import Cart
from .services import create_order_from_cart, update_order_delivery
from .serializers import OrderSerializer
from .models import Order
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
@api_view(['POST'])
def create_order_view(request):
    """
        Creates order

        This function handles order creation
    """

    try:
        cart = Cart.objects.get(user=request.user)
        order = create_order_from_cart(cart)
        response_data = {
            'success': True,
            'status': 201,
            'error': None,
            'message': 'Order created',
            'data': order.id,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    
    except Cart.DoesNotExist:
        response_data = {
            'success': False,
            'status': 404,
            'error': 'Not found',
            'message': 'Cart is empty',     
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)



@swagger_auto_schema(method='patch', request_body=OrderSerializer, 
                     responses={200: 'OK'})
@api_view(['PATCH'])
def update_order_status(request, order_id):
    """
        Updates delivery status

        This endpoint updates the delivery status of an order
    
    """

    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        response_data = {
            'success': False,
            'status': 404,
            'error': 'Not found',
            'message': 'Order not found',     
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)
    
    status = request.data.get('delivered')
    if not status:
        response_data = {
            'success': False,
            'status': 404,
            'error': 'Not found',
            'message': 'Please provide the order status.',     
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)
    
    update_order_delivery(order, status)
    serializer = OrderSerializer(order)
    response_data = {
        'success': True,
        'status': 200,
        'error': None,
        'message': 'Order status updated.',
        'data': serializer.data,
    }
    return Response(response_data, status=status.HTTP_200_OK)



@swagger_auto_schema(method='get', query_serializer=OrderSerializer, 
                     responses={200: 'OK'})
@api_view(['GET'])
def get_orders_by_users(request, user_id):
    """
        Retrieve orders by user

        This endpoint retrieves users order based on their id
    """

    try:
        orders = Order.objects.filter(user_id=user_id)
        serializer = OrderSerializer(orders, many=True)
        response_data = {
            'success': True,
            'status': 200,
            'error': None,
            'message': 'GET order by user successful.',
            'data': serializer.data,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Order.DoesNotExist:
        response_data = {
            'success': False,
            'status': 404,
            'error': 'Not found',
            'message': 'Orders not found',     
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)
    


@swagger_auto_schema(method='get', query_serializer=OrderSerializer, 
                     responses={200: 'OK', 400: 'Bad Request'})
@api_view(['GET'])
def get_order_by_id(request, order_id):
    """
        Retrieve order by order_id

        This endpoint retrieves single user order par order id
    """

    try:
        order = Order.objects.get(id=order_id)
        serializer = OrderSerializer(order)
        response_data = {
            'success': True,
            'status': 200,
            'error': None,
            'message': 'GET order by user successful.',
            'data': serializer.data,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Order.DoesNotExist:
        response_data = {
            'success': False,
            'status': 404,
            'error': 'Not found',
            'message': 'Order not found',     
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)
    


@swagger_auto_schema(method='patch', request_body=OrderSerializer, 
                     responses={200: 'OK', 400: 'Bad Request'})
@api_view(['PATCH'])
def cancel_order(request, order_id):
    """
        Cancel user order

        This endpoint cancels single user order par order id
    """
    
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        response_data = {
            'success': False,
            'status': 404,
            'error': 'Not found',
            'message': 'Order not found',     
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)
    
    order.status = order.CANCELED
    order.save()
    serializer = OrderSerializer(order)
    response_data = {
        'success': True,
        'status': 200,
        'error': None,
        'message': 'Order canceled successfully',
        'data': serializer.data,
    }
    return Response(response_data, status=status.HTTP_200_OK)
  


# @api_view(['DELETE'])
# def delete_order_item(request, order_item_id):
#     """This function deletes an item from an order usingv thme id"""
#     try:
#         order_item = OrderDetails.objects.get(id=order_item_id)
#     except OrderDetails.DoesNotExist:
#         return Response({"error": "Order item not found"}, status=status.HTTP_404_NOT_FOUND)
#     order_item.delete()
#     return Response({"message": "Order item deleted successfully"}, status=status.HTTP_200_OK)
