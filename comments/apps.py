"""
Comments App Configuration

Configuration class for the Comments app.
"""

from django.apps import AppConfig


class CommentsConfig(AppConfig):
    """
    Configuration for the Comments app.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "comments"
