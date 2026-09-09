from datetime import datetime

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient

from accounts.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture()
def common_user():
    user = get_user_model().objects.create(
        email="admin@admin.com", password="admin123", is_verified=True
    )
    return user


@pytest.mark.django_db
class TestPostApi:
    def setup_method(self):
        self.client = APIClient()

    def test_get_post_response_200(self, api_client):
        user = User.objects.create_user(
            email="testuser@test.com", password="testuserpass"
        )

        api_client.force_authenticate(user=user)
        url = reverse("blog:api-v1:post-list")
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401(self, api_client):
        # user = User.objects.create_user(email='testuser@test.com', password='testuserpass')
        # profile = Profile.objects.create(user=user)
        # self.client.force_authenticate(user)
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now().isoformat(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_response_201(self, api_client, common_user):
        # user = User.objects.create_user(email='testuser@test.com', password='testuserpass')
        # profile = Profile.objects.create(user=user)
        # self.client.force_authenticate(user)
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now().isoformat(),
        }
        # api_client.force_login(user=common_user)
        api_client.force_authenticate(common_user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_with_invalid_data_response_400(self, api_client, common_user):
        # user = User.objects.create_user(email='testuser@test.com', password='testuserpass')
        # profile = Profile.objects.create(user=user)
        # self.client.force_authenticate(user)
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
        }
        # api_client.force_login(user=common_user)
        api_client.force_authenticate(common_user)
        response = api_client.post(url, data)
        assert response.status_code == 400
