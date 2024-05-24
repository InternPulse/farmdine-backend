from django.urls import path, include
from .views import VendorRegisterView, RestaurantRegisterView, LoginView, UserDetailView, LogoutView

urlpatterns = [
    path('register-vendor', VendorRegisterView.as_view(), name='vendor-register'),
    path('register-restaurant', RestaurantRegisterView.as_view(), name='restaurant-register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user-detail/', UserDetailView.as_view(), name='user-detail'),
    path('logout/', LogoutView.as_view(), name='logout')
]