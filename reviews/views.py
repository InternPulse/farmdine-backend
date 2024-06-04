from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from products.models import Product
from accounts.models import CustomUser
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='post', query_serializer=ReviewSerializer, 
                     responses={200: 'OK', 400: 'Bad Request'})
@api_view(['POST'])
def create_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get', query_serializer=ReviewSerializer, 
                     responses={200: ReviewSerializer, 404: 'Not Found'})
@api_view(['GET'])
def get_reviews_for_product(request, product_id):
    reviews = Review.objects.filter(product_id=product_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='get', query_serializer=ReviewSerializer, 
                     responses={200: ReviewSerializer, 404: 'Not Found'})
@api_view(['GET'])
def get_reviews_by_user(request, user_id):
    reviews = Review.objects.filter(user_id=user_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='put', query_serializer=ReviewSerializer, 
                     responses={200: 'OK', 400: 'Bad Request'})
@api_view(['PUT'])
def update_review(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response({"detail": "Review not found."},
                        status=status.HTTP_404_NOT_FOUND)

    if review.user != request.user:
        return Response(
            {"detail": "You do not have permission to edit this review."},
            status=status.HTTP_403_FORBIDDEN
        )

    serializer = ReviewSerializer(review, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_review(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response({"detail": "Review not found."},
                        status=status.HTTP_404_NOT_FOUND)

    if review.user != request.user:
        return Response(
            {
                "detail": "You do not have permission to delete this review."},
            status=status.HTTP_403_FORBIDDEN)

    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
