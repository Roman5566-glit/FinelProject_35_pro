from django.contrib import admin

from .models import (
    Category,
    Brand,
    Product,
    ProductImage,
    Review,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin for Category"""
    list_display = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """Admin for Brand"""
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


class ProductImageInline(admin.TabularInline):
    """Inline for ProductImage"""
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin for Product"""
    list_display = (
        'id', 'name', 'category', 'brand',
        'price', 'stock', 'views',
        'is_active', 'created_at',
    )
    list_filter = ('is_active', 'category', 'brand')
    search_fields = ('name', 'description', 'sku')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    """Admin for ProductImage"""
    list_display = ('product', 'is_main')
    list_filter = ('is_main',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin for Review"""
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('product__name', 'user__username')
