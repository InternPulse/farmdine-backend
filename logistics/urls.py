from django.urls import path
from .views import get_logistics_details, update_logistics_status

urlpatterns = [
    path('logistics/<uuid:order_id>/', get_logistics_details, name='get_logistics_details'),
    path('logistics/<uuid:order_id>/status/', update_logistics_status, name='update_logistics_status'),
]
