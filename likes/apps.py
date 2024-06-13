"""
Likes App Configuration

Configuration class for the Likes app.
"""

from django.apps import AppConfig


class LikesConfig(AppConfig):
    """
    Configuration for the Likes app.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "likes"
