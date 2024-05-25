from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

CustomUser = get_user_model()

class EmailBackend(ModelBackend):
    """
    Authenticate using email address
    """

    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            # Try to fetch the user by email
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            # No user found, return None
            return None

        # Check if the password is valid
        if user.check_password(password):
            return user  # Return the user object if authentication succeeds
        return None  # Return None if authentication fails
