from rest_framework import status
from rest_framework.viewsets import ModelViewSet 
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductCreateView(ModelViewSet):
    """
        Add new product

        Add new product to the list
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)
    http_method_names = ['post']
    
    def create(self, request):
        if not request.user.is_vendor:
            response_data = {
                "success": False,
                "status": 403,
                "error": "you do not have permission to add product",
                "message": None,
            }
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            product = serializer.save(user=request.user)
            res = ProductSerializer(product, many=False)
            response_data = {
                "success": True,
                "status": 201,
                "error": None,
                "message": "product successfully added",
                "data": res.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListView(ModelViewSet):
    """
        Get all products

        Get the list of all products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']
    permission_classes = [AllowAny]


@permission_classes([AllowAny])
class ProductDetailView(APIView):
    """
        Get product details

        Get more information about a specific product
    """
    
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductSerializer(product)
            response_data = {
                "success": True,
                "status": 200,
                "error": None,
                "message": "product details found successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            response_data = {
                "success": False,
                "status": 404,
                "error": "product not found",
                "message": None,
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)


class ProductUpdateView(APIView):
    def put(self, request, product_id):
        """
            Update all product details

            Update all information about a specific product
        """
        try:
            product = Product.objects.get(id=product_id)
            if product.user != request.user:
                response_data = {
                    "success": False,
                    "status": 403,
                    "error": "you do not have permission to update this product",
                    "message": None,
                }
                return Response(response_data, status=status.HTTP_403_FORBIDDEN)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    "success": True,
                    "status": 200,
                    "error": None,
                    "message": "product successfully updated",
                    "data": serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            response_data = {
                "success": False,
                "status": 404,
                "error": "product not found",
                "message": None,
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, product_id):
        """
            Update some product details

            Update some information about a specific product
        """
        try:
            product = Product.objects.get(id=product_id)
            if product.user != request.user:
                response_data = {
                    "success": False,
                    "status": 403,
                    "error": "you do not have permission to update this product",
                    "message": None,
                }
                return Response(response_data, status=status.HTTP_403_FORBIDDEN)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    "success": True,
                    "status": 200,
                    "error": None,
                    "message": "product successfully updated",
                    "data": serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            response_data = {
                "success": False,
                "status": 404,
                "error": "product not found",
                "message": None,
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)


class ProductDeleteView(APIView):
    """
        Delete a product

        Delete a specific product from the list
    """
    def delete(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            if product.user != request.user:
                response_data = {
                    "success": False,
                    "status": 403,
                    "error": "you do not have permission to delete this product",
                    "message": None,
                }
                return Response(response_data, status=status.HTTP_403_FORBIDDEN)
            product.delete()
            response_data = {
                "success": True,
                "status": 200,
                "error": None,
                "message": "product successfully deleted",
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            response_data = {
                "success": False,
                "status": 404,
                "error": "product not found",
                "message": None,
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
