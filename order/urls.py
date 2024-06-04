from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_order_view, name="create order"),
    path('user/<str:user_id>', views.get_orders_by_users, name="user orders"),
    path('<str:order_id>', views.get_order_by_id, name="order by id"),
    path('<str:order_id>/status', views.update_order_status, name="update order status"),
    path('<str:order_id>/cancel', views.cancel_order, name="cancel order"),
    # path('order-items/<str:order_item_id>', views.delete_order_item, name="remove order item"),
]