from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Product
from .serializers import ProductSerializer
from drf_yasg.utils import swagger_auto_schema

class ProductListCreateAPIView(ListCreateAPIView):
    """Class-based view that handles GET (list) and POST requests for the product list"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    """Class-based view that handles GET (detail), PUT, and DELETE requests for individual products"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    
@swagger_auto_schema(methods=['get', 'post'], query_serializer=ProductSerializer, 
                     responses={200: ProductSerializer, 400: 'Bad Request'})
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods=['get','put'], query_serializer=ProductSerializer, 
                     responses={200: ProductSerializer, 400: 'Bad Request'})
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


