from django.urls import path
from .views import (
    create_review,
    get_reviews_for_product,
    get_reviews_by_user,
    update_review,
    delete_review
)

urlpatterns = [
    path(
        'api/reviews',
        create_review,
        name='create_review'),
    path(
        'api/reviews/product/<int:product_id>',
        get_reviews_for_product,
        name='get_reviews_for_product'),
    path(
        'api/reviews/user/<uuid:user_id>',
        get_reviews_by_user,
        name='get_reviews_by_user'),
    path(
        'api/reviews/<int:review_id>',
        update_review,
        name='update_review'),
    path(
        'api/reviews/<int:review_id>',
        delete_review,
        name='delete_review'),
]
