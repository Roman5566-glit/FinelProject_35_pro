from django.test import TestCase
from django.test import Client
from django.urls import reverse

from catalog.models import Category
from catalog.models import Brand
from catalog.models import Product


class CartTest(TestCase):
    """Tests for cart"""

    def setUp(self):
        """Setup test data"""
        self.client = Client()

        category = Category.objects.create(
            name='Phones',
            slug='phones'
        )

        brand = Brand.objects.create(
            name='Apple',
            slug='apple'
        )

        self.product = Product.objects.create(
            category=category,
            brand=brand,
            name='iPhone',
            slug='iphone',
            description='Phone',
            price=1000,
            stock=5,
            sku='IPHONE001'
        )

    def test_add_to_cart(self):
        """Test adding product to cart"""
        response = self.client.get(
            reverse(
                'cart_add',
                args=[self.product.id]
            )
        )
        self.assertEqual(response.status_code, 302)
