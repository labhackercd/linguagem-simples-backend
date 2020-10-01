from django.contrib.auth import get_user_model
from django.urls import reverse

import pytest
import responses
from mixer.backend.django import mixer
from rest_framework_simplejwt.tokens import RefreshToken
from .views import get_subjects, get_filter_subjects
from linguagemsimples.utils.scrape import Scrape
from django.conf import settings
from .mock_site_acompanhe import HTML_SCRAPE, HTML_FILE_VIDEO
from bs4 import BeautifulSoup
from rest_framework.exceptions import NotFound, ParseError
from django.utils.translation import gettext_lazy as _


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
    url = settings.API_DITEC + '/noticias/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('news')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_not_found_news(api_client, get_or_create_token):
    url = settings.API_DITEC + '/noticias/_search'
    responses.add(responses.POST,
                  url,
                  status=201)

    path = reverse('news')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': 'Error not found results'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_news(api_client, get_or_create_token):
    url = settings.API_DITEC + '/noticias/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('news-search') + '?search=word'
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_news_without_word(api_client, get_or_create_token):
    url = settings.API_DITEC + '/noticias/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('news-search')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': _('It is necessary to pass search')}
    assert len(responses.calls) == 0


@pytest.mark.django_db
@responses.activate
def test_radioagency(api_client, get_or_create_token):
    url = settings.API_DITEC + '/radioagencia/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('radioagency')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_not_found_radioagency(api_client, get_or_create_token):
    url = settings.API_DITEC + '/radioagencia/_search'
    responses.add(responses.POST,
                  url,
                  status=201)

    path = reverse('radioagency')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': 'Error not found results'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_radioagency(api_client, get_or_create_token):
    url = settings.API_DITEC + '/radioagencia/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('radioagency-search') + '?search=word'
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_radioagency_without_word(api_client, get_or_create_token):
    url = settings.API_DITEC + '/radioagencia/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('radioagency-search')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': _('It is necessary to pass search')}
    assert len(responses.calls) == 0


@pytest.mark.django_db
@responses.activate
def test_tvcamara(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-tv/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('tvcamara')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_not_found_tvcamara(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-tv/_search'
    responses.add(responses.POST,
                  url,
                  status=201)

    path = reverse('tvcamara')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': _('Error not found results')}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_tvcamara(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-tv/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('tvcamara-search') + '?search=word'
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_tvcamara_without_word(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-tv/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('tvcamara-search')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': _('It is necessary to pass search')}
    assert len(responses.calls) == 0


@pytest.mark.django_db
@responses.activate
def test_get_subjects(api_client, get_or_create_token):
    path = '/noticias/_search'
    responses.add(responses.POST,
                  settings.API_DITEC + path,
                  json={'response': 'json_test'}, status=201)

    response = get_subjects(path)

    assert response == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == settings.API_DITEC + \
        '/noticias/_search'


@pytest.mark.django_db
@responses.activate
def test_get_subjects_without_json(api_client, get_or_create_token):
    path = '/noticias/_search'

    responses.add(responses.POST,
                  settings.API_DITEC + path,
                  status=201)

    response = get_subjects(path)

    assert response == {'error': 'Error not found results'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == settings.API_DITEC + \
        '/noticias/_search'


@pytest.mark.django_db
@responses.activate
def test_get_filter_subjects(api_client, get_or_create_token):
    path = '/noticias/_search'
    responses.add(responses.POST,
                  settings.API_DITEC + path,
                  json={'response': 'json_test'}, status=201)

    response = get_filter_subjects('word', path)

    assert response == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == settings.API_DITEC + \
        '/noticias/_search'


@pytest.mark.django_db
@responses.activate
def test_get_filter_subjects_without_json(api_client, get_or_create_token):
    path = '/noticias/_search'

    responses.add(responses.POST,
                  settings.API_DITEC + path,
                  status=201)

    response = get_filter_subjects('word', path)

    assert response == {'error': _('Error not found results')}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == settings.API_DITEC + \
        '/noticias/_search'


@pytest.mark.django_db
@responses.activate
def test_radiocamara(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-radio/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('radiocamara')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_not_found_radiocamara(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-radio/_search'
    responses.add(responses.POST,
                  url,
                  status=201)

    path = reverse('radiocamara')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': _('Error not found results')}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_radiocamara(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-radio/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('radiocamara-search') + '?search=word'
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_radiocamara_without_word(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-radio/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('radiocamara-search')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': _('It is necessary to pass search')}
    assert len(responses.calls) == 0


@pytest.mark.django_db
@responses.activate
def test_video_session(api_client, get_or_create_token):
    url = 'https://www.camara.leg.br/evento-legislativo/1234'
    responses.add(responses.GET,
                  url,
                  body=HTML_SCRAPE,
                  status=200)
    path = reverse('videos-session', args=[1234])
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.status_code == 200
    assert len(responses.calls) == 1
    assert 'url' in response.json()[1]
    assert 'author' in response.json()[1]
    assert 'legend' in response.json()[1]
    assert 'schedule' in response.json()[1]
    assert 'duration' in response.json()[1]
    assert 'thumbnail' in response.json()[1]


@pytest.mark.django_db
@responses.activate
def test_video_session_dont_exist(api_client, get_or_create_token):
    url = 'https://www.camara.leg.br/evento-legislativo/1234'
    responses.add(responses.GET,
                  url,
                  status=404)
    path = reverse('videos-session', args=[1234])
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.status_code == 200
    assert len(responses.calls) == 1
    assert response.json() == {'error': _('Videos sessions not found!')}


@responses.activate
def test_get_webpage_videos():
    url = 'https://www.camara.leg.br/evento-legislativo/1234'
    responses.add(responses.GET,
                  url,
                  body=HTML_SCRAPE,
                  status=200)

    scrape = Scrape()
    response = scrape.get_webpage_videos(1234)

    assert response.status_code == 200
    assert len(responses.calls) == 1
    assert response.text == HTML_SCRAPE


def test_scraping_videos():
    scrape = Scrape()
    response = scrape.scraping_videos(HTML_SCRAPE)

    assert 'url' in response[1]
    assert 'author' in response[1]
    assert 'legend' in response[1]
    assert 'schedule' in response[1]
    assert 'duration' in response[1]
    assert 'thumbnail' in response[1]


def test_format_videos():
    scrape = Scrape()
    videos = scrape.scraping_videos(HTML_SCRAPE)
    soup = BeautifulSoup(HTML_SCRAPE, 'html.parser')
    videos = soup.find_all(class_='chamada__link-trecho linkReproduzir')

    response = scrape.format_videos(videos[0])

    assert 'url' in response
    assert 'author' in response
    assert 'legend' in response
    assert 'schedule' in response
    assert 'duration' in response
    assert 'thumbnail' in response


def test_error_format_videos():
    scrape = Scrape()
    response = scrape.format_videos('')

    assert 'error' in response
    assert response['error'] == 'Error get description'


@pytest.mark.django_db
@responses.activate
def test_file_video(api_client, get_or_create_token):
    url = 'https://www.camara.leg.br/evento-legislativo/59733/sessao/523169/video-trecho/1594254243193'  # NOQA
    responses.add(responses.GET,
                  url,
                  body=HTML_FILE_VIDEO,
                  status=200)

    path = reverse('file-video')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))

    data = {'url': url}
    response = api_client.post(path, data=data)

    assert response.json() == 'https://vod2.camara.leg.br/playlist/z7olw-vipoftz0fbfb_lra.mp4'  # NOQA

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_file_video_invalid_data(api_client, get_or_create_token):
    url = 'https://www.camara.leg.br/evento-legislativo/59733/sessao/523169/video-trecho/1594254243193'  # NOQA
    responses.add(responses.GET,
                  url,
                  body=HTML_FILE_VIDEO,
                  status=200)

    path = reverse('file-video')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))

    data = {'': ''}
    response = api_client.post(path, data=data)

    assert response.json() == {'url': ['Este campo é obrigatório.']}
    assert len(responses.calls) == 0


@pytest.mark.django_db
@responses.activate
def test_file_video_url_not_found(api_client, get_or_create_token):
    url = 'https://www.camara.leg.br/evento-legislativo/invalid_url'
    responses.add(responses.GET,
                  url,
                  body='',
                  status=400)

    path = reverse('file-video')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))

    data = {'url': url}
    response = api_client.post(path, data=data)

    assert response.json() == {'error': _('File video not found!')}
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@responses.activate
def test_get_file_video():
    url = 'https://www.camara.leg.br/evento-legislativo/59733/sessao/523169/video-trecho/1594254243193'  # NOQA
    responses.add(responses.GET,
                  url,
                  body=HTML_FILE_VIDEO,
                  status=200)

    scrape = Scrape()
    response = scrape.get_file_video(url)

    assert response.status_code == 200
    assert len(responses.calls) == 1
    assert response.text == HTML_FILE_VIDEO


def test_invalid_url_get_file_video():
    with pytest.raises(NotFound) as excinfo:
        url = 'https://www.invalid-url'
        scrape = Scrape()
        scrape.get_file_video(url)

    assert excinfo.typename == 'NotFound'
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == _('Invalid url information')


@responses.activate
def test_scraping_file_video():
    scrape = Scrape()
    response = scrape.scraping_file_video(HTML_FILE_VIDEO)

    assert response == 'https://vod2.camara.leg.br/playlist/z7olw-vipoftz0fbfb_lra.mp4'  # NOQA


def test_invalid_url_scraping_file_video():
    with pytest.raises(ParseError) as excinfo:
        scrape = Scrape()
        scrape.scraping_file_video('')

    assert excinfo.typename == 'ParseError'
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == _('Error parser file video')
