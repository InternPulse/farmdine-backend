from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer


# ViewSet to handle CRUD operations for reviews

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    # Ensure the review is saved with the current user as the author
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # Ensure users can only update their own reviews
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response({'error': 'You can only edit your own reviews'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    # Ensure users can only delete their own reviews
        def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response({'error': 'You can only delete your own reviews'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

    # View to get all reviews for a specific product
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def get_reviews_for_product(request, product_id):
        reviews = Review.objects.filter(product_id=product_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    # View to get all reviews by a specific user
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def get_reviews_by_user(request, user_id):
        reviews = Review.objects.filter(user_id=user_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
