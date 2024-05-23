from django.urls import path, include
from .views import VendorRegisterView

urlpatterns = [
    path('register/vendor', VendorRegisterView.as_view())
]