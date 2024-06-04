"""Contains all logics for manipulating the cart"""
from .models import Cart, CartItems
from .serializers import CartDetailSerializer, CartItemSerializers, CartSerializer
from products.models import Product

def add_to_cart(user_id, product_id, quantity=1):
    """This function handle services for adding to cart"""
    cart, created = Cart.objects.get_or_create(user_id=user_id)
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItems.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity = quantity
        cart_item.item_total_price = cart_item.product.price * cart_item.quantity
    else:
        cart_item.quantity = quantity
        cart_item.item_total_price = cart_item.product.price * cart_item.quantity
    cart_item.save()
    serialized_items = CartItemSerializers(cart_item).data
    return serialized_items


def remove_from_cart(user_id, product_id):
    """This function handles thme feature of removing items from thme cart"""
    try:
        cart = Cart.objects.get(user_id=user_id)
        cart_item = CartItems.objects.get(cart=cart, product_id=product_id)
        cart_item.delete()
    except (CartItems.DoesNotExist, Cart.DoesNotExist):
        pass
    serialized_item = CartItemSerializers(cart_item).data
    return serialized_item


def update_cart_item_quantity(user_id, product_id, quantity):
    """This function will update the cart quantity based on the new quantity set by user"""
    try:
        cart = Cart.objects.get(user_id=user_id)
        cart_item = CartItems.objects.get(cart=cart,product_id=product_id)
        cart_item.quantity = quantity
        cart_item.save()
    except CartItems.DoesNotExist:
        pass
    serialized_item = CartItemSerializers(cart_item).data
    return serialized_item


def get_cart_details(user_id):
    """This function handles the detailed view for the cart,
    allowing user to view cart item and price."""
    cart = Cart.objects.get(user_id=user_id)
    cart_items = CartItems.objects.filter(cart=cart)
    total_price = calculate_cart_total(cart)
    item_total_price = 0
    for item in cart_items:
        item.item_total_price = item.product.price * item.quantity
            
    serialized_items = CartItemSerializers(cart_items, many=True).data
        
    return {
        'items': serialized_items,
        'total_price': total_price,
    }

def clear_cart(user_id):
    """This function clears the cart when an order is placed"""
    cart = Cart.objects.get(user_id=user_id)
    cart.items.all().delete()


def calculate_cart_total(cart):
    """The function calculates thme total price of items in thme cart"""
    total_price = 0
    for item in cart.items.all():
        total_price += item.product.price * item.quantity
    return total_price
