from django.db import models
from accounts.models import CustomUser

# Model to store verification requests for vendors


class VendorVerification(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    request_date = models.DateTimeField(auto_now_add=True)
    verification_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return (
            f"{self.user.username} - "
            f"{'Verified' if self.is_verified else 'Not Verified'}"
        )
