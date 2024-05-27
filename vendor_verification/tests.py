from django.test import TestCase
from django.contrib.auth import get_user_model
from vendor_verification.models import VendorVerification

CustomUser = get_user_model()


class VendorVerificationTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

        def test_request_verification(self):
            verification = VendorVerification.objects.create(user=self.user)
            self.assertEqual(verification.user, self.user)
            self.assertFalse(verification.is_verified)
            self.assertIsNotNone(verification.request_date)
            self.assertIsNone(verification.verification_date)

            def test_verify_user(self):
                verification = VendorVerification.objects.create(
                    user=self.user)
                verification.is_verified = True
                verification.verification_date = timezone.now()
                verification.save()

                self.assertTrue(verification.is_verified)
                self.assertIsNotNone(verification.verification_date)
