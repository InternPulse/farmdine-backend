from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from products.models import Product
from accounts.models import CustomUser
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='post', query_serializer=ReviewSerializer, 
                     responses={200: 'OK'})
@api_view(['POST'])
def create_review(request):
    """
        Create Review

        Creates review of a product
    """
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        response_data = {
            'success': True,
            'status': 201,
            'error': None,
            'message': 'Review created successfully',
            'data': serializer.data,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    
    response_data = {
        'success': False,
        'status': 400,
        'error': serializer.errors,
        'message': 'Error creating review',
    }
    return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get', query_serializer=ReviewSerializer, 
                     responses={200: ReviewSerializer})
@api_view(['GET'])
def get_reviews_for_product(request, product_id):
    """
        GET reviews by product

        Retrieves reviews by product
    """
    reviews = Review.objects.filter(product_id=product_id)
    serializer = ReviewSerializer(reviews, many=True)
    response_data = {
        'success': True,
        'status': 200,
        'error': None,
        'message': 'Successfully retrieved product reviews',
        'data': serializer.data,
    }
    return Response(response_data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='get', query_serializer=ReviewSerializer, 
                     responses={200: ReviewSerializer})
@api_view(['GET'])
def get_reviews_by_user(request, user_id):
    """
        GET reviews by user

        Retrieves reviews of a user for products
    """
    reviews = Review.objects.filter(user_id=user_id)
    serializer = ReviewSerializer(reviews, many=True)
    response_data = {
        'success': True,
        'status': 200,
        'error': None,
        'message': 'Successfully retrieved reviews by user',
        'data': serializer.data,
    }
    return Response(response_data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='put', query_serializer=ReviewSerializer, 
                     responses={200: 'OK'})
@api_view(['PUT'])
def update_review(request, review_id):
    """
        Update Review

        Updates Review
    """
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        response_data = {
            'success': False,
            'status': 404,
            'error': 'Not found',
            'message': 'Review not found.',     
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    if review.user != request.user:
        response_data = {
            'success': False,
            'status': 403,
            'error': 'Forbidden',
            'message': 'You do not have permission to edit this review.',     
        }
        return Response(response_data, status=status.HTTP_403_FORBIDDEN)

    serializer = ReviewSerializer(review, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        response_data = {
            'success': True,
            'status': 200,
            'error': None,
            'message': 'Successfully updated review',
            'data': serializer.data,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    response_data = {
        'success': False,
        'status': 400,
        'error': serializer.errors,
        'message': 'Error updating review'
    }
    return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_review(request, review_id):
    """
        Delete Review

        Delete Review
    """
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        response_data = {
            'success': False,
            'status': 404,
            'error': 'Not found',
            'message': 'Review not found.',     
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    if review.user != request.user:
        response_data = {
            'success': False,
            'status': 403,
            'error': 'Forbidden',
            'message': 'You do not have permission to delete this review.',     
        }
        return Response(response_data, status=status.HTTP_403_FORBIDDEN)

    review.delete()
    response_data = {
        'success': True,
        'status': 204,
        'error': None,
        'message': 'Successfully deleted review'
    }
    return Response(status=status.HTTP_204_NO_CONTENT)
