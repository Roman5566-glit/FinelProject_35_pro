from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from orders.models import Order


def register_view(request):
    """Handle user registration"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {
            'form': form
        }
    )


@login_required
def profile(request):
    """Show user profile with orders"""
    orders = Order.objects.filter(
        user=request.user
    )

    return render(
        request,
        'accounts/profile.html',
        {
            'orders': orders
        }
    )
