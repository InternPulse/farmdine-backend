"""
Likes App URL Configuration

Defines the mapping between URL patterns and corresponding view functions or classes
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_like),
]
