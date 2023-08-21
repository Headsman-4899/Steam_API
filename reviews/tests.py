import json

from django.test import TestCase
from django.urls import reverse

from categories.models import Category
from developers.models import Developer
from games.models import Game
from publishers.models import Publisher
from system_requirements.models import SystemRequirement
from users.models import User
from reviews.models import Review


class ReviewModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="Test username",
                                        first_name="Test firstname",
                                        last_name="Test lastname",
                                        email="test@gmail.com",
                                        balance=0.0)
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
        self.review = Review.objects.create(
            comment="Test comment",
            point=4.0,
            user=self.user,
            game=self.game
        )

    def test_review_creation(self):
        self.assertEqual(self.review.comment, "Test comment")
        self.assertEqual(self.review.point, 4.0)
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.game, self.game)

    def test_review_str_representation(self):
        self.assertEqual(str(self.review), "Test comment")


class ReviewViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="Test user")
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
        self.review = Review.objects.create(
            comment="Test comment",
            point=4.0,
            user=self.user,
            game=self.game
        )
        self.base_url = reverse('review_list')
        self.detail_url = reverse('review_detail', args=[self.review.id])

    def test_review_list_view(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['review_list']), 1)

    def test_review_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['review_detail']['comment'], "Test comment")

    def test_review_create_view(self):
        new_review_data = {
            'comment': 'New comment',
            'point': 3.5,
            'user_id': self.user.id,
            'game_id': self.game.id
        }
        response = self.client.post(self.base_url, json.dumps(new_review_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_review_update_view(self):
        update_data = {
            'comment': 'Updated comment',
            'point': 4.8,
            'user_id': self.user.id,
            'game_id': self.game.id
        }
        response = self.client.put(self.detail_url, json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_review_delete_view(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 200)

