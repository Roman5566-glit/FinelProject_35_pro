from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True
    )

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Product(models.Model):
    def main_image(self):
        image = self.images.filter(
            is_main=True
        ).first()

        if image:
            return image

        return self.images.first()
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    sku = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )

    discount = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(100)]
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    views = models.PositiveIntegerField(
        default=0
    )

    meta_title = models.CharField(
        max_length=255,
        blank=True
    )

    meta_description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']

        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['price']),
            models.Index(fields=['is_active']),
            models.Index(fields=['created_at']),
        ]

        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    @property
    def final_price(self):
        return self.price - (
            self.price * self.discount / 100
        )


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(
        upload_to='products/'
    )

    is_main = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        ordering = ['-is_main']

        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товаров'

    def __str__(self):
        return f'{self.product.name} image'