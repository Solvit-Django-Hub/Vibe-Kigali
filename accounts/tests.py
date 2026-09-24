from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class AccountsTests(APITestCase):
    def test_register_creates_user(self):
        data = {
            'username': 'aline',
            'email': 'aline@example.com',
            'password': 'VibeKigali2026',
            'password2': 'VibeKigali2026',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='aline').exists())

    def test_register_rejects_mismatched_passwords(self):
        data = {
            'username': 'aline',
            'email': 'aline@example.com',
            'password': 'VibeKigali2026',
            'password2': 'SomethingElse2026',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_returns_tokens(self):
        User.objects.create_user(username='aline', password='VibeKigali2026')
        response = self.client.post(reverse('login'), {'username': 'aline', 'password': 'VibeKigali2026'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_profile_requires_authentication(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_profile_returns_logged_in_user(self):
        user = User.objects.create_user(username='aline', password='VibeKigali2026')
        self.client.force_authenticate(user=user)
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'aline')
