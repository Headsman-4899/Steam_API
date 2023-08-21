from django.test import TestCase
from django.urls import reverse

from categories.models import Category
from countries.models import Country
from developers.models import Developer
from publishers.models import Publisher
from system_requirements.models import SystemRequirement
from users.models import User
from games.models import Game
from .models import UserLibrary
import json


class UserLibraryModelTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="United States")
        self.user = User.objects.create(
            username="Test user",
            first_name="Test",
            last_name="User",
            email="testuser@example.com",
            balance=100.0,
            country=self.country
        )
        self.category = Category.objects.create(title="Test Category")
        self.developer = Developer.objects.create(title="Test Developer",
                                                  publisher=Publisher.objects.create(name="Test publisher", rating=5.0))
        self.system_requirement = SystemRequirement.objects.create(os="Test os",
                                                                   processor="Test processor",
                                                                   ram=8,
                                                                   video_card="Test video card",
                                                                   direct_x="Test direct x",
                                                                   disk_space=50)
        self.game = Game.objects.create(
            title="Test Game",
            description="Test description",
            cost=10.0,
            age_rating="Teen",
            rating=4.5,
            min_system_requirements=self.system_requirement,
            rec_system_requirements=self.system_requirement,
            developer=self.developer,
            category=self.category
        )
        self.user_library = UserLibrary.objects.create(user=self.user, game=self.game)

    def test_user_library_creation(self):
        self.assertEqual(self.user_library.user, self.user)
        self.assertEqual(self.user_library.game, self.game)

    def test_user_library_str_representation(self):
        expected_str = str(self.user_library.id)
        self.assertEqual(str(self.user_library), expected_str)


class UserLibraryViewsTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="United States")
        self.user = User.objects.create(
            username="Test user",
            first_name="Test",
            last_name="User",
            email="testuser@example.com",
            balance=100.0,
            country=self.country
        )
        self.category = Category.objects.create(title="Test Category")
        self.developer = Developer.objects.create(title="Test Developer",
                                                  publisher=Publisher.objects.create(name="Test publisher", rating=5.0))
        self.system_requirement = SystemRequirement.objects.create(os="Test os",
                                                                   processor="Test processor",
                                                                   ram=8,
                                                                   video_card="Test video card",
                                                                   direct_x="Test direct x",
                                                                   disk_space=50)
        self.game = Game.objects.create(
            title="Test Game",
            description="Test description",
            cost=10.0,
            age_rating="Teen",
            rating=4.5,
            min_system_requirements=self.system_requirement,
            rec_system_requirements=self.system_requirement,
            developer=self.developer,
            category=self.category
        )
        self.user_library = UserLibrary.objects.create(user=self.user, game=self.game)
        self.base_url = reverse('user_library_list')
        self.detail_url = reverse('user_library_detail', args=[self.user_library.id])

    def test_user_library_list_view(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['user_library_list']), 1)

    def test_user_library_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['user_library_detail']['id'], self.user_library.id)

    def test_user_library_create_view(self):
        new_user_library_data = {
            'is_favorite': True,
            'user_id': self.user.id,
            'game_id': self.game.id
        }
        response = self.client.post(self.base_url, json.dumps(new_user_library_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_user_library_update_view(self):
        update_data = {
            'total_time': 10.5,
            'is_favorite': True,
            'user_id': self.user.id,
            'game_id': self.game.id
        }
        response = self.client.put(self.detail_url, json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_user_library_delete_view(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 200)

