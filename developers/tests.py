from django.test import TestCase
from django.urls import reverse
from developers.models import Developer
from publishers.models import Publisher
import json


class DeveloperModelTestCase(TestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(name="Test Publisher")
        self.developer = Developer.objects.create(title="Test Developer", publisher=self.publisher)

    def test_developer_creation(self):
        self.assertEqual(self.developer.title, "Test Developer")
        self.assertEqual(self.developer.publisher, self.publisher)

    def test_developer_str_representation(self):
        self.assertEqual(str(self.developer), "Test Developer")


class DeveloperViewsTestCase(TestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(name="Test Publisher")
        self.developer = Developer.objects.create(title="Test Developer", publisher=self.publisher)
        self.base_url = reverse('developer_list')
        self.detail_url = reverse('developer_detail', args=[self.developer.id])

    def test_developer_list_view(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['developer_list']), 1)

    def test_developer_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)

    def test_developer_create_view(self):
        new_developer_data = {
            'title': 'New Developer',
            'publisher_id': self.publisher.id
        }
        response = self.client.post(self.base_url, json.dumps(new_developer_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_developer_update_view(self):
        update_data = {
            'title': 'Updated Developer',
            'publisher_id': self.publisher.id
        }
        response = self.client.put(self.detail_url, json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_developer_delete_view(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 200)

