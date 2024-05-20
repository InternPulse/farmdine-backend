from django.urls import path
from comments.views import (
    EventListCreate, EventDetail,
    CommentCreate, LikeCreate, LikeDelete
)
from products.views import ProductListCreate, ProductDetail

urlpatterns = [
    # Products URLs
    path('api/products/', ProductListCreate.as_view(), name='product-list-create'),
    path('api/products/<int:product_id>/', ProductDetail.as_view(), name='product-detail'),

    # Comments URLs
    path('events/<int:event_id>/comments/', CommentCreate.as_view(), name='comment-create'),
    path('comments/<int:comment_id>/likes/create/', LikeCreate.as_view(), name='like-create'),
    path('comments/<int:comment_id>/likes/delete/<int:pk>/', LikeDelete.as_view(), name='like-delete'),

    # Events URLs
    path('events/', EventListCreate.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),  
]
