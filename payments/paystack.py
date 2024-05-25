from django.conf import settings
import requests


base_url = "https://api.paystack.co/transaction/"
headers = {
    "Authorization": f"Bearer {settings.PAYSTACK_SEC_KEY}",
    "Content-Type": "application/json",
}


def make_payment(payment):
    url = base_url + "initialize"
    data = {
        "email": payment.email,
        "amount": int(payment.payment_amount * 100),  # Paystack expects amount in kobo
        "reference": str(payment.id),
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def verify_payment(reference):
    url = base_url + f"verify/{reference}"
    response = requests.get(url, headers=headers)
    return response.json()
