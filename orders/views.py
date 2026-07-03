from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from cart.cart import Cart
from .forms import OrderCreateForm
from .models import Order, OrderItem


@login_required
def order_create(request):
    """Create a new order"""
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            cart.clear()

            return redirect('/')

    else:
        form = OrderCreateForm()

    return render(
        request,
        'orders/order_create.html',
        {
            'form': form,
            'cart': cart
        }
    )


@login_required
def order_history(request):
    """Order history"""
    orders = (
        Order.objects
        .filter(user=request.user)
        .prefetch_related('items__product')
        .order_by('-created_at')
    )

    return render(
        request,
        'orders/order_history.html',
        {
            'orders': orders
        }
    )


@login_required
def order_detail(request, order_id):
    """Order detail"""
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(
        request,
        'orders/order_detail.html',
        {
            'order': order
        }
    )