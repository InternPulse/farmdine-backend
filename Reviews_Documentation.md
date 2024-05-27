### Reviews app Documentation

# Reviews and Ratings App Documentation

The Reviews and Ratings app provides endpoints to manage product reviews and ratings.

### Create Review
- **URL**: `/api/reviews`
- **Method**: `POST`
- **Description**: Write a review for a product.
- **Request Body**:
  ```json
  {
      "product": 1,
      "rating": 5,
      "review": "Excellent product!"
  }
  ```
- **Response**:
  - **Status Code**: `201 Created` with Review data.

### Get Reviews for Product
- **URL**: `/api/reviews/product/{product_id}`
- **Method**: `GET`
- **Description**: Retrieve all reviews for a specific product.
- **Response**:
  - **Status Code**: `200 OK` with list of Review data.

### Get Reviews by User
- **URL**: `/api/reviews/user/{user_id}`
- **Method**: `GET`
- **Description**: Retrieve all reviews written by a specific user.
- **Response**:
  - **Status Code**: `200 OK` with list of Review data.

### Update Review
- **URL**: `/api/reviews/{review_id}`
- **Method**: `PUT`
- **Description**: Update a review.
- **Request Body**:
  ```json
  {
      "rating": 4,
      "review": "Updated review text."
  }
  ```
- **Response**:
  - **Status Code**: `200 OK` with updated Review data.

### Delete Review
- **URL**: `/api/reviews/{review_id}`
- **Method**: `DELETE`
- **Description**: Delete a review.
- **Response**:
  - **Status Code**: `204 No Content
