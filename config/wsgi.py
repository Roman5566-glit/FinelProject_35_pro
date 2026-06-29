"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.contrib.auth import get_user_model
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

try:
    User = get_user_model()
    if not User.objects.filter(username='Admin').exists():
        User.objects.create_superuser('Admin', 'admin@example.com', '0000')
        print("Суперпользователь успешно создан!")
except Exception as e:
    print(f"Ошибка создания суперпользователя: {e}")