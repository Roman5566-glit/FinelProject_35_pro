from django.test import TestCase
from .models import Category
from .models import Brand
from .models import Product


class ProductModelTest(TestCase):
    """Tests for Product model"""

    def setUp(self):
        """Setup test data"""
        self.category = Category.objects.create(
            name='Phones',
            slug='phones'
        )
        self.brand = Brand.objects.create(
            name='Apple',
            slug='apple'
        )

    def test_create_product(self):
        """Test product creation"""
        product = Product.objects.create(
            category=self.category,
            brand=self.brand,
            name='iPhone',
            slug='iphone',
            description='Phone',
            price=1000,
            stock=5,
            sku='IPHONE001'
        )
        self.assertEqual(product.name, 'iPhone')

    def test_final_price(self):
        """Test discounted price"""
        product = Product.objects.create(
            category=self.category,
            brand=self.brand,
            name='MacBook',
            slug='macbook',
            description='Laptop',
            price=2000,
            stock=5,
            sku='MAC001',
            discount=10
        )
        self.assertEqual(product.final_price, 1800)
