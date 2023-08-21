from django.test import TestCase
from django.urls import reverse

from categories.models import Category
from countries.models import Country
from developers.models import Developer
from publishers.models import Publisher
from system_requirements.models import SystemRequirement
from users.models import User
from games.models import Game
from .models import UserDesiredGames
import json


class UserDesiredGamesModelTestCase(TestCase):
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
        self.desired_game = UserDesiredGames.objects.create(user=self.user, game=self.game)

    def test_desired_game_creation(self):
        self.assertEqual(self.desired_game.user, self.user)
        self.assertEqual(self.desired_game.game, self.game)

    def test_desired_game_str_representation(self):
        expected_str = str(self.desired_game.id)
        self.assertEqual(str(self.desired_game), expected_str)


class UserDesiredGamesViewsTestCase(TestCase):
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
        self.desired_game = UserDesiredGames.objects.create(user=self.user, game=self.game)
        self.base_url = reverse('user_desired_games_list')
        self.detail_url = reverse('user_desired_games_detail', args=[self.desired_game.id])

    def test_desired_games_list_view(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['user_desired_games_list']), 1)

    def test_desired_games_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['user_desired_game_detail']['id'], self.desired_game.id)

    def test_desired_games_create_view(self):
        new_desired_game_data = {
            'user_id': self.user.id,
            'game_id': self.game.id
        }
        response = self.client.post(self.base_url, json.dumps(new_desired_game_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_desired_games_update_view(self):
        update_data = {
            'user_id': self.user.id,
            'game_id': self.game.id
        }
        response = self.client.put(self.detail_url, json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_desired_games_delete_view(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 200)

