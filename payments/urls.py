from django.urls import path
from .views import MakePaymentView, VerifyPaymentView


urlpatterns = [
    path('make-payment/', MakePaymentView.as_view(), name='make-payment'),
    path('verify-payment/<str:reference>/', VerifyPaymentView.as_view(), name='verify-payment'),
]
