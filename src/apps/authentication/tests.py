import pytest
import json
from mixer.backend.django import mixer
from django.contrib.auth import get_user_model
from django.urls import reverse


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def test_password():
    return 'strong-test-pass'


@pytest.fixture
def get_jwt_response(api_client, test_password):
    user = mixer.blend(get_user_model())
    user.set_password(test_password)
    user.save()
    data = {
        'username': user.username,
        'password': test_password
    }
    url = reverse('token-create')
    response = api_client.post(url, data=data)
    return response


@pytest.mark.django_db
def test_user_models():
    user = mixer.blend(get_user_model(), username='joao')
    assert get_user_model().objects.count() == 1
    assert user.__str__() == 'joao'


@pytest.mark.django_db
def test_apps():
    from apps.authentication.apps import AuthenticationConfig
    assert AuthenticationConfig.name == 'authentication'


@pytest.mark.django_db
def test_obtain_token_url(get_jwt_response):
    response = get_jwt_response
    assert response.status_code == 200


@pytest.mark.django_db
def test_refresh_token_url(api_client, get_jwt_response):
    request = json.loads(get_jwt_response.content)
    data = {
        'refresh': request['refresh']
    }
    url = reverse('token-refresh')
    response = api_client.post(url, data=data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_verify_token_url(api_client, get_jwt_response):
    request = json.loads(get_jwt_response.content)
    data = {
        'token': request['access']
    }
    url = reverse('token-verify')
    response = api_client.post(url, data=data)
    assert response.status_code == 200
