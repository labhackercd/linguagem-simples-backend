from django.contrib.auth import get_user_model
from django.urls import reverse

import pytest
import responses
from mixer.backend.django import mixer
from rest_framework_simplejwt.tokens import RefreshToken
from .views import ListNews, SearchNews
from django.conf import settings


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
def test_name_app():
    from apps.api_ditec.apps import ApiDitecConfig
    assert ApiDitecConfig.name == 'api_ditec'


@pytest.mark.django_db
@responses.activate
def test_news(api_client, get_or_create_token):
    responses.add(responses.POST,
                  settings.API_DITEC + '/noticias/_search',
                  json={'response': 'json_test'}, status=201)

    url = reverse('news')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(url)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == settings.API_DITEC + '/noticias/_search'  # NOQA


@pytest.mark.django_db
@responses.activate
def test_not_found_news(api_client, get_or_create_token):
    responses.add(responses.POST,
                  settings.API_DITEC + '/noticias/_search',
                  status=201)

    url = reverse('news')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(url)

    assert response.json() == {'error': 'Error not found news'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == settings.API_DITEC + '/noticias/_search'  # NOQA


@pytest.mark.django_db
@responses.activate
def test_get_news(api_client, get_or_create_token):
    responses.add(responses.POST,
                  settings.API_DITEC + '/noticias/_search',
                  json={'response': 'json_test'}, status=201)

    listNews = ListNews()

    response = listNews.get_news()

    assert response == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == settings.API_DITEC + '/noticias/_search'  # NOQA


@pytest.mark.django_db
@responses.activate
def test_search_news(api_client, get_or_create_token):
    responses.add(responses.POST,
                  settings.API_DITEC + '/noticias/_search',
                  json={'response': 'json_test'}, status=201)

    url = reverse('news-search') + '?search=word'
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(url)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == settings.API_DITEC + '/noticias/_search'  # NOQA


@pytest.mark.django_db
@responses.activate
def test_search_news_without_word(api_client, get_or_create_token):
    responses.add(responses.POST,
                  settings.API_DITEC + '/noticias/_search',
                  json={'response': 'json_test'}, status=201)

    url = reverse('news-search')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(url)

    assert response.json() == {'error': 'It is necessary to pass search'}
    assert len(responses.calls) == 0


@pytest.mark.django_db
@responses.activate
def test_get_filter_news(api_client, get_or_create_token):
    responses.add(responses.POST,
                  settings.API_DITEC + '/noticias/_search',
                  json={'response': 'json_test'}, status=201)

    listNews = SearchNews()

    response = listNews.get_filter_news('word')

    assert response == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == settings.API_DITEC + '/noticias/_search'  # NOQA


@pytest.mark.django_db
@responses.activate
def test_error_get_filter_news(api_client, get_or_create_token):
    responses.add(responses.POST,
                  settings.API_DITEC + '/noticias/_search',
                  status=201)

    listNews = SearchNews()

    response = listNews.get_filter_news('word')

    assert response == {'error': 'Error not found news'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == settings.API_DITEC + '/noticias/_search'  # NOQA
