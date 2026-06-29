from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    """Form for creating orders"""

    class Meta:
        """Meta options for OrderCreateForm"""
        model = Order
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'city',
            'address',
        )
