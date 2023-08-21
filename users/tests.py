from django.test import TestCase
from django.urls import reverse
from users.models import User
from countries.models import Country
import json


class UserModelTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="United States")
        self.user = User.objects.create(
            username="testuser",
            first_name="Test",
            last_name="User",
            email="testuser@example.com",
            balance=100.0,
            country=self.country
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertEqual(self.user.balance, 100.0)
        self.assertEqual(self.user.country, self.country)

    def test_user_str_representation(self):
        expected_str = "testuser"
        self.assertEqual(str(self.user), expected_str)


class UserViewsTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="United States")
        self.user = User.objects.create(
            username="testuser",
            first_name="Test",
            last_name="User",
            email="testuser@example.com",
            balance=100.0,
            country=self.country
        )
        self.base_url = reverse('user_list')
        self.detail_url = reverse('user_detail', args=[self.user.id])

    def test_user_list_view(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['user_list']), 1)

    def test_user_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['user_detail']['username'], "testuser")

    def test_user_create_view(self):
        new_user_data = {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'newuser@example.com',
            'balance': 50.0,
            'country_id': self.country.id
        }
        response = self.client.post(self.base_url, json.dumps(new_user_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_user_update_view(self):
        update_data = {
            'username': 'updateduser',
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updateduser@example.com',
            'balance': 150.0,
            'country_id': self.country.id
        }
        response = self.client.put(self.detail_url, json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_user_delete_view(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 200)

