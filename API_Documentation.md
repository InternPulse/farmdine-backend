# Farmdine Backend API Documentation

## Introduction

This document provides detailed information about the Farmdine Backend API, which is used to manage products, events, comments, and likes.

## Products Endpoints

### Create Product

- URL: `/products`
- Method: `POST`
- Description: Add a new product.
- Request Body:
  json
  {
    "name": "Example Product",
    "description": "This is an example product.",
    "price": 19.99,
    "stock": 50
  }
  
- Response:
  - Status Code: `201 Created`
  - Body: Newly created product object.

### Retrieve All Products

- URL: `/products`
- Method: `GET`
- Description: Retrieve all products.
- Response:
  - Status Code: `200 OK`
  - Body: Array of product objects.

### Retrieve a Product by ID

- URL: `/products/{product_id}`
- Method: `GET`
- Description: Retrieve a product by its ID.
- Response:
  - Status Code: `200 OK`
  - Body: Product object.

### Update a Product

- URL: `/products/{product_id}`
- Method: `PUT`
- Description: Update a product's details.
- Request Body:
  json
  {
    "name": "Updated Product Name",
    "description": "Updated product description.",
    "price": 29.99,
    "stock": 100
  }
  
- Response:
  - Status Code: `200 OK`
  - Body: Updated product object.

### Delete a Product

- URL: `/products/{product_id}`
- Method: `DELETE`
- Description: Remove a product.
- Response:
  - Status Code: `204 No Content`

## Comments Endpoints

### Add a Comment to an Event

- URL: `/events/{event_id}/comments`
- Method: `POST`
- Description: Add a comment to an event.
- Request Body:
  json
  {
    "text": "This is a new comment."
  }
  
- Response:
  - Status Code: `201 Created`
  - Body: Newly created comment object.

### Like a Comment

- URL: `/comments/{comment_id}/likes`
- Method: `POST`
- Description: Add a like to a comment.
- Request Body:
  json
  {
    "user": 1
  }
  
- Response:
  - Status Code: `201 Created`
  - Body: Newly created like object.

### Unlike a Comment

- URL: `/comments/{comment_id}/likes/{like_id}`
- Method: `DELETE`
- Description: Remove a like from a comment.
- Response:
  - Status Code: `204 No Content`
