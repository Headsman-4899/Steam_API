from django.test import TestCase
from django.urls import reverse
from countries.models import Country
import json


class CountryModelTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Test Country")

    def test_country_creation(self):
        self.assertEqual(self.country.name, "Test Country")

    def test_country_str_representation(self):
        self.assertEqual(str(self.country), "Test Country")


class CountryViewsTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Test Country")
        self.base_url = reverse('country_list')
        self.detail_url = reverse('country_detail', args=[self.country.id])

    def test_country_list_view(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['country_list']), 1)

    def test_country_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['country_detail']['name'], "Test Country")

    def test_country_create_view(self):
        new_country_data = {
            'name': 'New Country'
        }
        response = self.client.post(self.base_url, json.dumps(new_country_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_country_update_view(self):
        update_data = {
            'name': 'Updated Country'
        }
        response = self.client.put(self.detail_url, json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_country_delete_view(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 200)

