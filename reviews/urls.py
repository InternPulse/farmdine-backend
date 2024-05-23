from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, get_reviews_for_product, get_reviews_by_user

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'', ReviewViewSet, basename='review')

# URL configurations for the reviews app
urlpatterns = [
    path('product/<int:product_id>/', get_reviews_for_product,
         name='get_reviews_for_product'),
    path('user/<int:user_id>/', get_reviews_by_user, name='get_reviews_by_user'),
    path('', include(router.urls)),
]
