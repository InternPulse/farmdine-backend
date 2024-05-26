from django.test import TestCase
from django.contrib.auth import get_user_model
from products.models import Product
from reviews.models import Review

CustomUser = get_user_model()


class ReviewsTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            stock=100
        )

    def test_create_review(self):
        review = Review.objects.create(
            user=self.user,
            product=self.product,
            rating=5,
            review='Great product!'
        )
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.product, self.product)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.review, 'Great product!')
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)

    def test_update_review(self):
        review = Review.objects.create(
            user=self.user,
            product=self.product,
            rating=5,
            review='Great product!'
        )
        review.rating = 4
        review.review = 'Good product.'
        review.save()

        updated_review = Review.objects.get(id=review.id)
        self.assertEqual(updated_review.rating, 4)
        self.assertEqual(updated_review.review, 'Good product.')
        self.assertNotEqual(
            updated_review.created_at,
            updated_review.updated_at)
