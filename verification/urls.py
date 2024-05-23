from django.urls import path
from .views import request_verification, get_verification_status

# URL configurations for the verification app

urlpatterns = [
    path('request/', request_verification, name='request_verification'),
    path('<int:user_id>/', get_verification_status,
         name='get_verification_status'),
]
