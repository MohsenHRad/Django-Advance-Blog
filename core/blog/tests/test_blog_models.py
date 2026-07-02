from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Post, Profile


class TestPostModel(TestCase):

    def test_create_post_with_valid_data(self):
        user = get_user_model().objects.create_user(email='mmd@test.com', password='mmd123')
        profile = Profile.objects.create(
            user=user,
            first_name='mmd',
            last_name='rad'
        )
        post_obj = Post.objects.create(
            author=profile,
            title='test',
            content='description',
            status=True,
            category=None,
            published_date=datetime.now()
        )
        self.assertEqual(post_obj.title, 'test')
