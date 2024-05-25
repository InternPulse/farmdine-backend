# Farmdine Backend API Documentation

## Introduction

This document provides detailed information about the Farmdine Backend API, which is used to manage User Management and Authentication.

## Accounts App 
Handles CustomUser registeration, login, logout, CRUD and Authentication of user. 

### Authentication
- Djangorestframework_simple-jwt is implemented for CustomUser authentication
- run `migrate` command to migrate rest_framework_simplejwt.token_blacklist models
### Account app Folder structure
- ...
- authentication_backends.py: overrides django default authentication to use email to login
- ...

### Accounts Model Structure
#### CustomUser Model
- extends AbstractUser
- fields include: - id (UUID FIELD)
                  - all AbstractUser fields
                  - is_vendor
                  - is_restaurant
                  - phone_number
#### VendorProfile Model
- extends models.Model
- fields include: - vendor: OnetoOne Field. Vendor is a primary key (pk). CustomUser ID same as VendorProfile pk
                  - business_name 
                  - vendor_address

#### RestaurantProfile Model
- extends models.Model
- fields include: - resturant: OnetoOne Field. Vendor is a primary key (pk). CustomUser ID same as RestaurantProfile pk 
                  - business_name 
                  - resturant_address

### Accounts Endpoints
##### Vendor Register
- URL: `/api/accounts/register-vendor`
- Method: `POST`
- Description: Add a register a Vendor CustomUser.
- Request Body:
  json
{
    "user": {
        "username": "brain",
        "email": "brain@gmail.com",
        "first_name": "brian",
        "last_name": "ant",
        "phone_number": null
    },
    "vendor_profile": {
        "vendor": "67abec6d-061e-404e-a5fd-b971b61cb97b",
        "business_name": "Vatint",
        "vendor_address": "no 23c st"
    }
}
- Response:
  - Status Code: `201 Created`

##### Restaurant Register
- URL: `/api/accounts/register-restuarant`
- Method: `POST`
- Description: Add a register a Restaurant CustomUser.
- Request Body:
  json
{
    "user": {
        "username": "brain",
        "email": "brain@gmail.com",
        "first_name": "brian",
        "last_name": "ant",
        "phone_number": null
    },
    "restaurant_profile": {
        "vendor": "67abec6d-061e-404e-a5fd-b971b61cb97b",
        "business_name": "Vatint",
        "restaurant_address": "no 23c st"
    }
}
- Response:
  - Status Code: `201 Created`

##### Login
- URL: `/api/accounts/register-restuarant`
- Method: `POST`
- Description: Add a register a Restaurant CustomUser.
- Request Body:
  json 
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzE2Mjg5NCwiaWF0IjoxNzE2NTU4MDk0LCJqdGkiOiI2OWI5NWJjNzQ1YzI0OTA3ODg0Mjk0ZmE1ZTFkOGU0YyIsInVzZXJfaWQiOiI2N2FiZWM2ZC0wNjFlLTQwNGUtYTVmZC1iOTcxYjYxY2I5N2IifQ.cimCvdP2Pn7L4wdtS2Yh03oyqKejaCLp0yB2rIUaGJU",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NjQ0NDk0LCJpYXQiOjE3MTY1NTgwOTQsImp0aSI6ImQ5ZDJiNmEwYzVjODRkMTNiNDlhOTEyMjViNTU4ZjExIiwidXNlcl9pZCI6IjY3YWJlYzZkLTA2MWUtNDA0ZS1hNWZkLWI5NzFiNjFjYjk3YiJ9._bUyD2vl0CNq6qPtjsmKIdJieh60VUXXwPDlFdDYBtA"
}
- Response: 
  - Status Code: `200 OK`

##### Get User
- URL: `/api/accounts/user-detail`
- Method: `GET`
- Description: Retrieve a specific user.
- Request Body:
json
{
    "username": "brain",
    "email": "brain@gmail.com",
    "first_name": "brian",
    "last_name": "ant",
    "phone_number": null
}
- Response:
  - Status Code: `200 OK`

##### Update User
- URL: `/api/accounts/user-detail`
- Method: `PUT`
- Description: Updates user field. Note that this endpoint updates only CustomUser Model
- Request Body:
json
{
    "username": "collins",
    "email": "admin@hotmail.org",
    "first_name": "brian",
    "last_name": "ant",
    "phone_number": "3929832032"
}
- Response:
  - Status Code: `200 OK`

##### Delete User 
- URL: `/api/accounts/user-detail`
- Method: `DELETE`
- Description: Delete a user instance
- Response:
  - Status Code: `204 No content`

##### Logout User
- URL: `/api/accounts/logout`
- METHOD: `POST`
- Description: Log user out. Blacklists refresh token
- Response:
  - Status Code: `204 No content`

### Serializers
- List of serializers found within accounts.serializers:
- CustomUserSerializer
- VendorProfileSerializer
- RestaurantProfileSerializer
- LogoutSerializer


