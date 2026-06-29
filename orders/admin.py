from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """Inline for order items"""
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin config for orders"""
    list_display = (
        'id',
        'user',
        'status',
        'paid',
        'created_at',
    )
    list_filter = (
        'status',
        'paid',
    )
    inlines = [OrderItemInline]
