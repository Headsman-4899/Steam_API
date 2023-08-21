from django.test import TestCase
from django.urls import reverse
from publishers.models import Publisher
import json


class PublisherModelTestCase(TestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(name="Test Publisher", rating=4.0)

    def test_publisher_creation(self):
        self.assertEqual(self.publisher.name, "Test Publisher")
        self.assertEqual(self.publisher.rating, 4.0)

    def test_publisher_str_representation(self):
        self.assertEqual(str(self.publisher), "Test Publisher")


class PublisherViewsTestCase(TestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(name="Test Publisher", rating=4.0)
        self.base_url = reverse('publisher_list')
        self.detail_url = reverse('publisher_detail', args=[self.publisher.id])

    def test_publisher_list_view(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['publisher_list']), 1)

    def test_publisher_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['publisher_detail']['name'], "Test Publisher")

    def test_publisher_create_view(self):
        new_publisher_data = {
            'name': 'New Publisher',
            'rating': 3.5
        }
        response = self.client.post(self.base_url, json.dumps(new_publisher_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_publisher_update_view(self):
        update_data = {
            'name': 'Updated Publisher',
            'rating': 4.2
        }
        response = self.client.put(self.detail_url, json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_publisher_delete_view(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 200)

