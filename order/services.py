"""This module handle features for order management"""
from cart.services import calculate_cart_total, clear_cart
from .models import Order, OrderDetails

def create_order_from_cart(cart):
    """This function create user order based on items on the cart"""
    total_amount = calculate_cart_total(cart)

    order = Order.objects.create(
        user = cart.user,
        total_amount = total_amount,
        status = 'Ordered', # Initially set status to false
        delivered = False,
    )

    for item in cart.items.all():
        OrderDetails.objects.create(
            orderID = order,
            productID = item.product,
            quantity = item.quantity,
            price = item.product.price * item.quantity
        )
    # This marks the order as successfully placed
    order.save()

    clear_cart(cart.user.id) # Clear the cart once the order is placed
    return order


def update_order_delivery(order, status):
    """This function updates the delivery status once an order is delivered"""
    order.delivered = status
    order.save()

