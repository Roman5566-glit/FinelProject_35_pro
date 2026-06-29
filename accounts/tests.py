from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class UserModelTest(TestCase):
    """Tests for User model"""

    def test_create_user(self):
        """Test user creation"""
        user = User.objects.create_user(
            username='admin',
            password='12345'
        )
        self.assertEqual(user.username, 'admin')
        self.assertTrue(user.check_password('12345'))
