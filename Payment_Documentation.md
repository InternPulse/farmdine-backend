## Payment app Documentation
The Payment app provides endpoints to initiate and verify payment.


### Make Payment
- **URL**: `/api/payments/make-payment/`
- **Method**: `POST`
- **Description**: Initiate payment for ordered items.
- **Request Body**:
  ```json
  {
    "email": "johndoe@example.com",
    "payment_amount": 20500
  }
  ```
- **Response**:
  - **Status Code**: `200 OK` with data to fulfill the payment.


### Verify Payment
- **URL**: `/api/payments/verify-payment/{reference}`
- **Method**: `GET`
- **Description**: Verify payment to ensure transaction was successful.
- **Response**:
  - **Status Code**: `200 OK` with payment data.
