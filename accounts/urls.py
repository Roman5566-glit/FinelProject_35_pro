from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from .views import register_view, profile


urlpatterns = [
    path(
        'register/',
        register_view,
        name='register'
    ),

    path(
        'login/',
        LoginView.as_view(
            template_name='accounts/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    path(
        'profile/',
        profile,
        name='profile'
    ),
]

"""URL patterns for accounts app"""
