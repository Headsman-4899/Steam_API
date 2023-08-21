from django.test import TestCase
from django.urls import reverse
from games.models import Game
from categories.models import Category
from developers.models import Developer
from publishers.models import Publisher
from system_requirements.models import SystemRequirement
import json


class GameModelTestCase(TestCase):
    def setUp(self):
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

    def test_game_creation(self):
        self.assertEqual(self.game.title, "Test Game")
        self.assertEqual(self.game.description, "Test description")
        self.assertEqual(self.game.cost, 10.0)
        self.assertEqual(self.game.age_rating, "Teen")
        self.assertEqual(self.game.rating, 4.5)
        self.assertEqual(self.game.min_system_requirements, self.system_requirement)
        self.assertEqual(self.game.rec_system_requirements, self.system_requirement)
        self.assertEqual(self.game.developer, self.developer)
        self.assertEqual(self.game.category, self.category)

    def test_game_str_representation(self):
        self.assertEqual(str(self.game), "Test Game")


class GameViewsTestCase(TestCase):
    def setUp(self):
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
        self.base_url = reverse('game_list')
        self.detail_url = reverse('game_detail', args=[self.game.id])

    def test_game_list_view(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['games']), 1)

    def test_game_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['game_detail']['title'], "Test Game")

    def test_game_create_view(self):
        new_game_data = {
            'title': 'New Game',
            'description': 'New description',
            'cost': 20.0,
            'age_rating': 'Mature',
            'rating': 3.5,
            'min_system_requirements_id': self.system_requirement.id,
            'rec_system_requirements_id': self.system_requirement.id,
            'developer_id': self.developer.id,
            'category_id': self.category.id
        }
        response = self.client.post(self.base_url, json.dumps(new_game_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_game_update_view(self):
        update_data = {
            'title': 'Updated Game',
            'description': 'Updated description',
            'cost': 15.0,
            'age_rating': 'Everyone',
            'rating': 4.0,
            'min_system_requirements_id': self.system_requirement.id,
            'rec_system_requirements_id': self.system_requirement.id,
            'developer_id': self.developer.id,
            'category_id': self.category.id
        }
        response = self.client.put(self.detail_url, json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_game_delete_view(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 200)

