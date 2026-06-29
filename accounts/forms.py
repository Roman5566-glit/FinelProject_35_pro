from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    """User registration form"""
    email = forms.EmailField()

    class Meta:
        """Meta options for RegisterForm"""
        model = User
        fields = (
            'username',
            'email',
            'phone',
            'city',
            'password1',
            'password2',
        )
