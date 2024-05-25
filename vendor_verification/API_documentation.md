# Verification App

## Endpoints

### Request Verification
- **URL**: `/api/verification`
- **Method**: `POST`
- **Description**: Request verification for a vendor.
- **Response**: 
  - **Status Code**: `201 Created` with VendorVerification data.

### Get Verification Status
- **URL**: `/api/verification/{user_id}`
- **Method**: `GET`
- **Description**: Retrieve the verification status of a vendor.
- **Response**: 
  - **Status Code**: `200 OK` with VendorVerification data.
