from . import views
from django.urls import path

urlpatterns = [
    path('add/<str:user_id>', views.add_to_cart_view, name="add to cart"),
    path('remove/<str:user_id>', views.remove_from_cart_view, name="remove from cart"),
    path('update/<str:user_id>', views.update_cart_item_quantity_view, name="update cart item quantity"),
    path('clear/<str:user_id>', views.clear_cart_view, name="clear cart"),
    path('<str:user_id>', views.view_cart, name="view cart"),
]