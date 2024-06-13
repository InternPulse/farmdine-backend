from rest_framework import status, generics
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer
from cart.serializers import Cart
from .paystack import make_payment, verify_payment


# Create your views here.
class MakePaymentView(generics.CreateAPIView):
    """
        Initiate payment for items added to cart

        Adds payment details to the database before making an API call to PayStack to initiate payment
    """
    serializer_class = PaymentSerializer
    def post(self, request):
        data = request.data
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            try:
                cart = Cart.objects.get(id=data['cart_id'])
                # save payment data
                payment = Payment.objects.create(**data, cart=cart, payment_amount=data['payment_amount'])

                # call the make_payment function
                payment_res = make_payment(payment)
                if payment_res.status_code == 200:
                    response_data = {
                        "success": True,
                        "status": 200,
                        "error": None,
                        "message": "Payment initialized successfully",
                        "data": payment_res.json()
                    }
                    return Response(response_data, status=status.HTTP_200_OK)
                else:
                    response_data = {
                        "success": False,
                        "status": payment_res.status_code,
                        "error": "Payment initialization failed",
                        "message": None,
                        "data": payment_res.json()
                    }
                    payment.delete()
                    return Response(response_data, status=payment_res.status_code)
            except Cart.DoesNotExist:
                response_data = {
                    "success": False,
                    "status": 404,
                    "error": "Cart not found",
                    "message": None,
                }
                return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyPaymentView(generics.ListAPIView):
    """
        Verify payment for items added to cart

        Gets payment or reference id from the receipt sent to user, then sends an API request to PayStack to verify payment status.
    """
    serializer_class = PaymentSerializer
    def get(self, request, reference):
        # call the verify_payment function
        payment_status = verify_payment(reference)
        if payment_status.status_code == 200:
            data = payment_status.json()
            if data['status'] and data['data']['status'] == 'success':
                payment = Payment.objects.get(id=reference)
                payment.verified = True
                payment.save()
                response_data = {
                    "success": True,
                    "status": 200,
                    "error": None,
                    "message": "Payment verified successfully",
                    "data": data['data']
                }
                return Response(response_data, status=status.HTTP_200_OK)
            response_data = {
                "success": False,
                "status": 402,
                "error": "Payment is yet to be made",
                "message": None,
                "data": data['data']
            }
            return Response(response_data, status=status.HTTP_402_PAYMENT_REQUIRED)
        response_data = {
            "success": False,
            "status": payment_status.status_code,
            "error": "Payment is yet to be made",
            "message": None,
            "data": payment_status.json()
        }
        return Response(response_data, status=payment_status.status_code)
