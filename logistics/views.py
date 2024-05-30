from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Logistics
from .serializers import LogisticsSerializer

@api_view(['GET'])
def get_logistics_details(request, order_id):
    try:
        logistics = Logistics.objects.get(order_id=order_id)
        serializer = LogisticsSerializer(logistics)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Logistics.DoesNotExist:
        return Response({"error": "Logistics details not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_logistics_status(request, order_id):
    try:
        logistics = Logistics.objects.get(order_id=order_id)
    except Logistics.DoesNotExist:
        return Response({"error": "Logistics details not found"}, status=status.HTTP_404_NOT_FOUND)

    new_status = request.data.get('status')
    if new_status not in dict(Logistics.STATUS_CHOICES).keys():
        return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

    logistics.status = new_status
    logistics.save()
    serializer = LogisticsSerializer(logistics)
    return Response(serializer.data, status=status.HTTP_200_OK)

