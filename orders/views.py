from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem


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
