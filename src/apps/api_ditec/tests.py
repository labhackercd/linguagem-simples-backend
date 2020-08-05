from django.contrib.auth import get_user_model
from django.urls import reverse

import pytest
import responses
from mixer.backend.django import mixer
from rest_framework_simplejwt.tokens import RefreshToken
from .views import ListNews, SearchNews


@pytest.fixture
def get_or_create_token():
    user = mixer.blend(get_user_model())
    refresh = RefreshToken.for_user(user)
    return refresh.access_token


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
@responses.activate
def test_news(api_client, get_or_create_token):
    responses.add(responses.POST, 'http://es-hom.camara.gov.br:9200/noticias/_search',
                  json={'response': 'json_test'}, status=201)

    url = reverse('news-list')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(url)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://es-hom.camara.gov.br:9200/noticias/_search'


@pytest.mark.django_db
@responses.activate
def test_not_found_news(api_client, get_or_create_token):
    responses.add(responses.POST, 'http://es-hom.camara.gov.br:9200/noticias/_search',
                  status=201)

    url = reverse('news-list')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(url)

    assert response.json() == {'error': 'Error not found news'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://es-hom.camara.gov.br:9200/noticias/_search'


@pytest.mark.django_db
@responses.activate
def test_get_news(api_client, get_or_create_token):
    responses.add(responses.POST, 'http://es-hom.camara.gov.br:9200/noticias/_search',
                  json={'response': 'json_test'}, status=201)

    listNews = ListNews()

    response = listNews.get_news()

    assert response == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://es-hom.camara.gov.br:9200/noticias/_search'


@pytest.mark.django_db
@responses.activate
def test_get_filter_news(api_client, get_or_create_token):
    responses.add(responses.POST, 'http://es-hom.camara.gov.br:9200/noticias/_search',
                  json={'response': 'json_test'}, status=201)

    listNews = SearchNews()

    response = listNews.get_filter_news('word')

    assert response == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://es-hom.camara.gov.br:9200/noticias/_search'
