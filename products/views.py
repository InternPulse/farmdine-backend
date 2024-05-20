# products/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.exceptions import NotFound

class ProductListCreate(generics.ListCreateAPIView):
    """
    View to list all products or create a new product.
    - GET: Return a list of all products.
    - POST: Create a new product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a product instance.
    - GET: Return the details of a specific product.
    - PUT: Update a specific product.
    - DELETE: Delete a specific product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        try:
            return Product.objects.get(id=self.kwargs.get('product_id'))
        except Product.DoesNotExist:
            raise NotFound(detail=f"Product with id {self.kwargs.get('product_id')} not found.")

    def delete(self, request, *args, **kwargs):
        """Delete a specific product."""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        """Update a specific product."""
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

