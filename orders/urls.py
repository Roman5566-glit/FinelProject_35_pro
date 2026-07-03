from django.urls import path

from .views import (
    order_create,
    order_history,
    order_detail,
)

urlpatterns = [
    path(
        'create/',
        order_create,
        name='order_create'
    ),

    path(
        'history/',
        order_history,
        name='order_history'
    ),

    path(
        '<int:order_id>/',
        order_detail,
        name='order_detail'
    ),
]