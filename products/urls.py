from django.urls import path
from .views import ProductListCreate, ProductDetail

urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:product_id>/', ProductDetail.as_view(), name='product-detail'),
]
