from decimal import Decimal
from catalog.models import Product


class Cart:
    """Shopping cart"""

    def __init__(self, request):
        """Init cart"""
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        """Add product to cart"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """Save cart"""
        self.session.modified = True

    def update(self, product, quantity):
        """Update product quantity"""
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity
            self.save()

    def remove(self, product):
        """Remove product from cart"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """Clear cart"""
        self.session['cart'] = {}
        self.save()

    def __len__(self):
        """Return total items"""
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        """Iterate over cart items"""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            if 'product' not in item:
                continue
            item['price'] = Decimal(item['product'].price)
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def get_total_price(self):
        """Return total price"""
        return sum(
            Decimal(item['product'].price) * item['quantity']
            for item in self
        )
