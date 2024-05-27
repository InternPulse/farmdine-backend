from rest_framework import status, generics
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer
from .paystack import make_payment, verify_payment


# Create your views here.
class MakePaymentView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    def post(self, request):
        data = request.data
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            payment = serializer.save()
            # call the make_payment fuction
            payment_res =  make_payment(payment)
            if payment_res.status_code == 200:
                return Response(payment_res.json(), status=status.HTTP_200_OK)
            else:
                payment.delete()
                return Response(payment_res.json(), status=payment_res.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyPaymentView(generics.ListAPIView):
    def get(self, request, reference):
        # call the verify_pament fuction
        payment_status = verify_payment(reference)
        if payment_status.status_code == 200:
            data = payment_status.json()
            if data['status'] and data['data']['status'] == 'success':
                payment = Payment.objects.get(id=reference)
                payment.verified = True
                payment.save()
                return Response(data['data'], status=status.HTTP_200_OK)
            return Response(data['data'], status=status.HTTP_402_PAYMENT_REQUIRED)
        return Response(payment_status.json(), status=payment_status.status_code)
