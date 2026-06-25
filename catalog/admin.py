from django.contrib import admin

from .models import (
    Category,
    Brand,
    Product,
    ProductImage
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'parent',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

    search_fields = (
        'name',
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

    search_fields = (
        'name',
    )


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'brand',
        'price',
        'stock',
        'views',
        'is_active',
        'created_at',
    )

    list_filter = (
        'is_active',
        'category',
        'brand',
    )

    search_fields = (
        'name',
        'description',
        'sku',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

    inlines = [
        ProductImageInline
    ]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'is_main',
    )

    list_filter = (
        'is_main',
    )