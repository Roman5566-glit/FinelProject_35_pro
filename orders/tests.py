from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Order

User = get_user_model()


class OrderTest(TestCase):
    """Test case for orders"""

    def test_create_order(self):
        """Test order creation"""
        user = User.objects.create_user(
            username='ivan',
            password='12345678'
        )

        order = Order.objects.create(
            user=user,
            first_name='Ivan',
            last_name='Ivanov',
            email='ivan@test.com',
            phone='+380991112233',
            city='Kyiv',
            address='Main street 1'
        )

        self.assertEqual(order.first_name, 'Ivan')
        self.assertEqual(order.city, 'Kyiv')
        self.assertFalse(order.paid)
        self.assertEqual(order.status, 'new')
