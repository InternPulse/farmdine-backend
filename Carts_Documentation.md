# Cart Management API

Cart Management API for FarmDine e-commerce platform. The API provides endpoints for managing user carts, including adding, removing, updating, and clearing cart items.

## Features

- Add items to cart
- Remove items from cart
- Update item quantities in cart
- View cart details
- Clear cart


## API Endpoints

### Add Item to Cart

- **URL:** `api/cart/<str:user_id>/add/`
- **Method:** `POST`
- **Description:** Adds an item to the cart.
- **Request Body:**
    ```json
    {
        "product_id": "product_uuid",
        "quantity": 1
    }
    ```
- **Response:**
    ```json
    {
        "message": "Item added to cart",
        "cart_details": {...}
    }
    ```

### Remove Item from Cart

- **URL:** `api/cart/<str:user_id>/remove/`
- **Method:** `DELETE`
- **Description:** Removes an item from the cart.
- **Request Body:**
    ```json
    {
        "product_id": "product_uuid"
    }
    ```
- **Response:**
    ```json
    {
        "message": "Item removed from cart",
        "cart_details": {...}
    }
    ```

### Update Cart Item Quantity

- **URL:** `api/cart/<str:user_id>/update/`
- **Method:** `PUT`
- **Description:** Updates the quantity of an item in the cart.
- **Request Body:**
    ```json
    {
        "product_id": "product_uuid",
        "quantity": 2
    }
    ```
- **Response:**
    ```json
    {
        "message": "Cart item quantity updated",
        "cart_details": {...}
    }
    ```

### Clear Cart

- **URL:** `api/cart/<str:user_id>/clear/`
- **Method:** `DELETE`
- **Description:** Clears all items from the cart.
- **Response:**
    ```json
    {
        "message": "Cart cleared"
    }
    ```

### View Cart

- **URL:** `api/cart/<str:user_id>`
- **Method:** `GET`
- **Description:** Retrieves the details of the cart.
- **Response:**
    ```json
    {
        "items": [...],
        "total_price": 0.00
    }
    ```

## Models

### Cart

- **Fields:**
    - `id` (UUID): Primary key
    - `user` (ForeignKey to CustomUser): User who owns the cart
    - `created_at` (DateTime): Timestamp when the cart was created

### CartItems

- **Fields:**
    - `id` (UUID): Primary key
    - `cart` (ForeignKey to Cart): Cart to which the item belongs
    - `product` (ForeignKey to Product): Product added to the cart
    - `quantity` (PositiveInteger): Quantity of the product
    - `added_at` (DateTime): Timestamp when the item was added to the cart

## Running Tests

To run the tests for the cart management feature, use the following command:

```sh
python manage.py test cart
