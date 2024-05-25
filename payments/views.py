from rest_framework import status, generics
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer
from .paystack import make_payment, verify_payment


# Create your views here.
class MakePaymentView(generics.CreateAPIView):
    def post(self, request):
        data = request.data
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            payment = serializer.save()
            # call the makepayment fuction
            initiate_payment =  make_payment(payment)
            if initiate_payment.status_code == 200:
                return Response(initiate_payment.response.json(), status=status.HTTP_200_OK)
            else:
                return Response(initiate_payment.response.json(), status=initiate_payment.response.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyPaymentView(generics.ListAPIView):
    def get(self, request, reference):
        # call the verify_pament fuction
        payment_status = verify_payment(reference)
        if payment_status.response.status_code == 200:
            data = payment_status.response.json()
            if data['status'] and data['data']['status'] == 'success':
                try:
                    payment = Payment.objects.get(id=reference)
                    payment.verified = True
                    payment.save()
                    return Response(data, status=status.HTTP_200_OK)
                except Payment.DoesNotExist:
                    return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(payment_status.response.json(), status=payment_status.response.status_code)
