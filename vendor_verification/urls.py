from django.urls import path
from .views import request_verification, get_verification_status

urlpatterns = [
    path('',
         request_verification, name='request_verification'),
    path('status/<uuid:user_id>',
         get_verification_status, name='get_verification_status'),
]
