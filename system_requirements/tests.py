from django.test import TestCase
from django.urls import reverse
from system_requirements.models import SystemRequirement
import json


class SystemRequirementModelTestCase(TestCase):
    def setUp(self):
        self.system_requirement = SystemRequirement.objects.create(
            os="Windows 10",
            processor="Intel Core i7",
            ram=16,
            video_card="NVIDIA GeForce GTX 1080",
            direct_x="11",
            disk_space=50
        )

    def test_system_requirement_creation(self):
        self.assertEqual(self.system_requirement.os, "Windows 10")
        self.assertEqual(self.system_requirement.processor, "Intel Core i7")
        self.assertEqual(self.system_requirement.ram, 16)
        self.assertEqual(self.system_requirement.video_card, "NVIDIA GeForce GTX 1080")
        self.assertEqual(self.system_requirement.direct_x, "11")
        self.assertEqual(self.system_requirement.disk_space, 50)

    def test_system_requirement_str_representation(self):
        expected_str = "Windows 10 Intel Core i7 NVIDIA GeForce GTX 1080"
        self.assertEqual(str(self.system_requirement), expected_str)


class SystemRequirementViewsTestCase(TestCase):
    def setUp(self):
        self.system_requirement = SystemRequirement.objects.create(
            os="Windows 10",
            processor="Intel Core i7",
            ram=16,
            video_card="NVIDIA GeForce GTX 1080",
            direct_x="11",
            disk_space=50
        )
        self.base_url = reverse('system_requirements_list')
        self.detail_url = reverse('system_requirements_detail', args=[self.system_requirement.id])

    def test_system_requirement_list_view(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['system_requirements_list']), 1)

    def test_system_requirement_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['system_requirements_detail']['os'], "Windows 10")

    def test_system_requirement_create_view(self):
        new_system_requirement_data = {
            'os': 'Linux',
            'processor': 'AMD Ryzen 5',
            'ram': 8,
            'video_card': 'AMD Radeon RX 580',
            'direct_x': '12',
            'disk_space': 40
        }
        response = self.client.post(self.base_url, json.dumps(new_system_requirement_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_system_requirement_update_view(self):
        update_data = {
            'os': 'macOS',
            'processor': 'Apple M1',
            'ram': 16,
            'video_card': 'Integrated',
            'direct_x': 'N/A',
            'disk_space': 30
        }
        response = self.client.put(self.detail_url, json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_system_requirement_delete_view(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 200)


