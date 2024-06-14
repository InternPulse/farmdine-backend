from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Logistics
from .serializers import LogisticsSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='get', query_serializer=LogisticsSerializer, 
                     responses={200: LogisticsSerializer, 400: 'Bad Request'})
@api_view(['GET'])
def get_logistics_details(request, order_id):
    """
    Retrieve logistics details for a specific order.

    Args:
        request: The HTTP request object.
        order_id (int): The ID of the order to retrieve logistics details for.

    Returns:
        Response: A Response object containing the logistics details or an error message.
    """
    try:
        logistics = Logistics.objects.get(order_id=order_id)
        serializer = LogisticsSerializer(logistics)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Logistics.DoesNotExist:
        return Response({"error": "Logistics details not found"}, status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(method='put', request_body=LogisticsSerializer, 
                     responses={200: 'OK', 400: 'Bad Request'})
@api_view(['PUT'])
def update_logistics_status(request, order_id):
    """
    Update the logistics status for a specific order.

    Args:
        request: The HTTP request object containing the new status.
        order_id (int): The ID of the order to update the logistics status for.

    Returns:
        Response: A Response object containing the updated logistics details or an error message.
    """
    try:
        logistics = Logistics.objects.get(order_id=order_id)
    except Logistics.DoesNotExist:
        return Response({"error": "Logistics details not found"}, status=status.HTTP_404_NOT_FOUND)

    new_status = request.data.get('status')
    if not new_status or new_status not in dict(Logistics.STATUS_CHOICES).keys():
        return Response({"error": "Invalid or missing status"}, status=status.HTTP_400_BAD_REQUEST)

    logistics.status = new_status
    logistics.save()
    serializer = LogisticsSerializer(logistics)
    return Response(serializer.data, status=status.HTTP_200_OK)
