from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Post, Profile


class TestPostModel(TestCase):
    def setUp(self):
        self.user = user = get_user_model().objects.create_user(email='mmd@test.com', password='mmd123')
        self.profile = profile = Profile.objects.create(
            user=self.user,
            first_name='mmd',
            last_name='rad'
        )

    def test_create_post_with_valid_data(self):
        post_obj = Post.objects.create(
            author=self.profile,
            title='test',
            content='description',
            status=True,
            category=None,
            published_date=datetime.now()
        )
        self.assertTrue(Post.objects.filter(pk=post_obj.id).exists())
        self.assertEqual(Post.objects.filter(pk=post_obj.pk).exists(), True)
        self.assertEqual(post_obj.title, 'test')
