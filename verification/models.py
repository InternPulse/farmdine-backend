from django.db import models
from django.conf import settings

# Model to store verification requests for vendors


class VendorVerification(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    is_verified = models.BooleanField(default=False)
    requested_at = models.DateTimeField(auto_now_add=True)
