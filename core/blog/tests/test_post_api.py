from datetime import datetime

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from accounts.models import User


@pytest.mark.django_db
class TestPostApi:
    def setup_method(self):
        self.client = APIClient()

    def test_get_post_response_200(self):
        user = User.objects.create_user(email='testuser@test.com', password='testuserpass')

        self.client.force_authenticate(user=user)
        url = reverse('blog:api-v1:post-list')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401(self):
        # user = User.objects.create_user(email='testuser@test.com', password='testuserpass')
        # profile = Profile.objects.create(user=user)
        # self.client.force_authenticate(user)
        url = reverse('blog:api-v1:post-list')
        data = {
            'title': 'test',
            'content': 'description',
            'status': True,
            'published_date': datetime.now().isoformat()
        }
        response = self.client.post(url, data)
        assert response.status_code == 401
