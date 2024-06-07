from . import views
from django.urls import path

urlpatterns = [
    path('<str:user_id>/add', views.add_to_cart_view, name="add to cart"),
    path('<str:user_id>/remove', views.remove_from_cart_view, name="remove from cart"),
    path('<str:user_id>/update', views.update_cart_item_quantity_view, name="update cart item quantity"),
    path('<str:user_id>/clear', views.clear_cart_view, name="clear cart"),
    path('<str:user_id>', views.view_cart, name="view cart"),
]