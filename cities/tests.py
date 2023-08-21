from django.test import TestCase
from django.urls import reverse
from cities.models import City
from countries.models import Country
import json


class CityModelTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Test Country")
        self.city = City.objects.create(name="Test City", country=self.country)

    def test_city_creation(self):
        self.assertEqual(self.city.name, "Test City")
        self.assertEqual(self.city.country, self.country)

    def test_city_str_representation(self):
        self.assertEqual(str(self.city), "Test City")


class CityViewsTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Test Country")
        self.city = City.objects.create(name="Test City", country=self.country)
        self.base_url = reverse('city_list')
        self.detail_url = reverse('city_detail', args=[self.city.id])

    def test_city_list_view(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['city_list']), 1)

    def test_city_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['city_detail']['name'], "Test City")

    def test_city_create_view(self):
        new_city_data = {
            'name': 'New City',
            'country_id': self.country.id
        }
        response = self.client.post(self.base_url, json.dumps(new_city_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_city_update_view(self):
        update_data = {
            'name': 'Updated City',
            'country_id': self.country.id
        }
        response = self.client.put(self.detail_url, json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_city_delete_view(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 200)
