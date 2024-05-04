from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

CustomUser = get_user_model()

class CustomUserModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'password': 'test_password',
            'is_superuser': False,
            'is_staff': False,
            'is_verified': True,
        }
        self.user = CustomUser.objects.create_user(**self.user_data)

    def test_user_creation(self):
        """Test CustomUser model creation"""
        self.assertTrue(isinstance(self.user, CustomUser))
        self.assertEqual(self.user.email, self.user_data['email'])
        self.assertTrue(self.user.check_password(self.user_data['password']))
        self.assertFalse(self.user.is_superuser)
        self.assertFalse(self.user.is_staff)
        self.assertTrue(self.user.is_verified)
        self.assertIsNotNone(self.user.date_joined)

    def test_get_token(self):
        """Test get_token method"""
        token_data = self.user.get_token()
        self.assertIn('access', token_data)
        self.assertIn('refresh', token_data)
        access_token = token_data['access']
        refresh_token = token_data['refresh']
        self.assertIsInstance(access_token, str)
        self.assertIsInstance(refresh_token, str)
