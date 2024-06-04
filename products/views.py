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

