from django.test import TestCase
from django.urls import reverse
from categories.models import Category
import json


class CategoryModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title="Test Category")

    def test_category_creation(self):
        self.assertEqual(self.category.title, "Test Category")
        self.assertIsNone(self.category.main_category)

    def test_category_str_representation(self):
        self.assertEqual(str(self.category), "Test Category")


class CategoryViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title="Test Category")
        self.base_url = reverse('category_list')
        self.detail_url = reverse('category_detail', args=[self.category.id])

    def test_category_list_view(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['category_list']), 1)

    def test_category_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['category_detail']['title'], "Test Category")

    def test_category_create_view(self):
        new_category_data = {
            'title': 'New Category'
        }
        response = self.client.post(self.base_url, json.dumps(new_category_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_category_update_view(self):
        update_data = {
            'title': 'Updated Category'
        }
        response = self.client.put(self.detail_url, json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_category_delete_view(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 200)
