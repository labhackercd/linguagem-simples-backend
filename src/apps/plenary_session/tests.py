import pytest
from mixer.backend.django import mixer
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.urls import reverse
import json
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from .models import PlenarySession, Publication, SavedContent


@pytest.fixture
def get_or_create_token():
    user = mixer.blend(get_user_model())
    refresh = RefreshToken.for_user(user)
    return refresh.access_token


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def create_plenary_session():
    author = mixer.blend(get_user_model())
    plenary_session = PlenarySession.objects.create(author=author,
                                                    location='plenary',
                                                    date=datetime.now(),
                                                    type_session='virtual',
                                                    situation_session='next_topic',  # NOQA
                                                    resume='resume of session',
                                                    enable=True)
    return plenary_session


@pytest.mark.django_db
def test_apps():
    from apps.plenary_session.apps import PlenarySessionConfig
    assert PlenarySessionConfig.name == 'plenary_session'


@pytest.mark.django_db
def test_plenary_session_create():
    mixer.blend(PlenarySession)
    assert PlenarySession.objects.count() == 1


@pytest.mark.django_db
def test_plenary_session_str():
    plenary_session = mixer.blend(PlenarySession, date=datetime.now(),
                                  type_session='virtual')
    assert plenary_session.__str__() == 'virtual - ' + \
        datetime.now().strftime("%d/%m/%Y")


@pytest.mark.django_db
def test_plenary_session_create_erro_location(create_plenary_session):
    with pytest.raises(ValidationError) as excinfo:
        plenary_session = create_plenary_session
        plenary_session.location = 'ERROR'
        plenary_session.full_clean()
    assert '{\'location\': ["Valor \'ERROR\' não é uma opção válida."]}' in (
        str(excinfo))


@pytest.mark.django_db
def test_plenary_session_create_erro_date(create_plenary_session):
    with pytest.raises(ValidationError) as excinfo:
        plenary_session = create_plenary_session
        plenary_session.date = 'ERROR'
        plenary_session.full_clean()
    assert 'date' in str(excinfo)


@pytest.mark.django_db
def test_plenary_session_create_erro_type_session(create_plenary_session):
    with pytest.raises(ValidationError) as excinfo:
        plenary_session = create_plenary_session
        plenary_session.type_session = 'ERROR'
        plenary_session.full_clean()
    assert '{\'type_session\': ["Valor \'ERROR\' não é uma opção válida."]}' in (  # NOQA
        str(excinfo))


@pytest.mark.django_db
def test_plenary_session_create_erro_situation_session(create_plenary_session):
    with pytest.raises(ValidationError) as excinfo:
        plenary_session = create_plenary_session
        plenary_session.situation_session = 'ERROR'
        plenary_session.full_clean()
    assert '{\'situation_session\': ["Valor \'ERROR\' não é uma opção válida."]}' in (  # NOQA
        str(excinfo))


@pytest.mark.django_db
def test_plenary_session_create_none_location():
    with pytest.raises(IntegrityError):
        mixer.blend(PlenarySession, location=None)


@pytest.mark.django_db
def test_plenary_session_create_none_date():
    with pytest.raises(IntegrityError):
        mixer.blend(PlenarySession, date=None)


@pytest.mark.django_db
def test_plenary_session_create_none_type_session():
    with pytest.raises(IntegrityError):
        mixer.blend(PlenarySession, type_session=None)


@pytest.mark.django_db
def test_plenary_session_create_none_situation_session():
    with pytest.raises(IntegrityError):
        mixer.blend(PlenarySession,
                    situation_session=None)


@pytest.mark.django_db
def test_plenary_session_create_none_resume():
    with pytest.raises(IntegrityError):
        mixer.blend(PlenarySession, resume=None)


@pytest.mark.django_db
def test_session_plenary_create_url(api_client, get_or_create_token):
    data = {'location': 'plenary',
            'date': datetime.today().strftime('%Y-%m-%d'),
            'type_session': 'virtual',
            'situation_session': 'pre_session',
            'resume': 'Resume of session',
            'enable': 'True'}
    url = reverse('sessions-list')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.post(url, data=data)
    request = json.loads(response.content)
    assert response.status_code == 201
    assert request['location'] == 'plenary'
    assert request['date'] == datetime.now().strftime('%Y-%m-%d')
    assert request['type_session'] == 'virtual'
    assert request['situation_session'] == 'pre_session'
    assert request['resume'] == 'Resume of session'


@pytest.mark.django_db
def test_session_plenary_detail_url(api_client, get_or_create_token):
    plenary_session = mixer.blend(PlenarySession)
    url = reverse('sessions-detail', args=[plenary_session.id])
    data = {'situation_session': 'closed_session'}
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.patch(url, data=data)
    request = json.loads(response.content)
    assert response.status_code == 200
    assert request['id'] == plenary_session.id


@pytest.mark.django_db
def test_session_plenary_update_url(api_client, get_or_create_token):
    plenary_session = mixer.blend(PlenarySession,
                                  situation_session='pre_session')
    url = reverse('sessions-detail', args=[plenary_session.id])
    data = {'situation_session': 'closed_session'}
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.patch(url, data=data)
    request = json.loads(response.content)
    assert response.status_code == 200
    assert request['situation_session'] == 'closed_session'


@pytest.mark.django_db
def test_session_plenary_delete_url(api_client, get_or_create_token):
    plenary_session = mixer.blend(PlenarySession)
    url = reverse('sessions-detail', args=[plenary_session.id])
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.delete(url)
    assert response.status_code == 204
    assert PlenarySession.objects.count() == 0


@pytest.mark.django_db
def test_publication_create():
    mixer.blend(Publication)
    assert Publication.objects.count() == 1


@pytest.mark.django_db
def test_publication_integrity_error():
    with pytest.raises(IntegrityError) as excinfo:
        mixer.blend(Publication, content='', tweet_id=None, image=None)
    assert 'not_content_tweet_image_null' in str(excinfo.value)


@pytest.mark.django_db
def test_publication_validation_error():
    with pytest.raises(ValidationError) as excinfo:
        user = mixer.blend(get_user_model())
        session = mixer.blend(PlenarySession, enable=True)
        publication = Publication.objects.create(author=user, session=session)
        publication.clean()
    assert 'Content or tweet_id or image are required' in str(excinfo.value)


@pytest.mark.django_db
def test_publication_validation_error_disable_session():
    with pytest.raises(ValidationError) as excinfo:
        user = mixer.blend(get_user_model())
        session = mixer.blend(PlenarySession, enable=False)
        publication = Publication.objects.create(author=user, session=session)
        publication.clean()
    assert 'Only session enable can have publication' in str(excinfo.value)


@pytest.mark.django_db
def test_publication_str():
    publication = mixer.blend(Publication)
    assert publication.__str__() == '%s' % (
        timezone.now().strftime("%d/%m/%Y, %H:%M:%S"))


@pytest.mark.django_db
def test_publication_create_url(api_client, get_or_create_token):
    session = mixer.blend(PlenarySession, enable=True)

    data = {
        'title': 'teste',
        'image': '',
        'tweet_id': '',
        'content': 'teste',
        'session': session.id
    }

    url = reverse('publications-list')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.post(url, data=data)
    request = json.loads(response.content)
    assert response.status_code == 201
    assert request['title'] == 'teste'
    assert request['content'] == 'teste'
    assert request['state'] == 'published'


@pytest.mark.django_db
def test_publication_validate_required_fields(api_client, get_or_create_token):
    session = mixer.blend(PlenarySession)
    data = {
        'image': '',
        'tweet_id': '',
        'content': '',
        'session': session.id
    }
    url = reverse('publications-list')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.post(url, data=data)
    request = json.loads(response.content)
    assert response.status_code == 400
    assert request['non_field_errors'] == [
        'Content or tweet_id or image are required']


@pytest.mark.django_db
def test_publication_keyerror_content(api_client, get_or_create_token):
    session = mixer.blend(PlenarySession)
    data = {
        'image': '',
        'tweet_id': '',
        'session': session.id
    }
    url = reverse('publications-list')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.post(url, data=data)
    request = json.loads(response.content)
    assert response.status_code == 400
    assert request['non_field_errors'] == [
        "'content' are required in json object"]


@pytest.mark.django_db
def test_publication_keyerror_image(api_client, get_or_create_token):
    session = mixer.blend(PlenarySession)
    data = {
        'content': '',
        'tweet_id': '',
        'session': session.id
    }
    url = reverse('publications-list')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.post(url, data=data)
    request = json.loads(response.content)
    assert response.status_code == 400
    assert request['non_field_errors'] == [
        "'image' are required in json object"]


@pytest.mark.django_db
def test_publication_keyerror_tweet_id(api_client, get_or_create_token):
    session = mixer.blend(PlenarySession)
    data = {
        'content': '',
        'image': '',
        'session': session.id
    }
    url = reverse('publications-list')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.post(url, data=data)
    request = json.loads(response.content)
    assert response.status_code == 400
    assert request['non_field_errors'] == [
        "'tweet_id' are required in json object"]


@pytest.mark.django_db
def test_publication_update_url(api_client, get_or_create_token):
    publication = mixer.blend(Publication)
    data = {
        'state': 'inactive'
    }
    url = reverse('publications-detail', args=[publication.id])
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.patch(url, data=data)
    request = json.loads(response.content)
    assert response.status_code == 200
    assert request['state'] == 'inactive'


@pytest.mark.django_db
def test_session_plenary_ordering_desc_url(api_client, get_or_create_token):
    ORDER_DESC = '?ordering=-date'
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    mixer.blend(PlenarySession, date=yesterday)
    mixer.blend(PlenarySession, date=today)
    url = reverse('sessions-list') + ORDER_DESC
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(url)
    respose_json = json.loads(response.content)
    assert response.status_code == 200
    assert respose_json[0]['date'] == today.strftime('%Y-%m-%d')


@pytest.mark.django_db
def test_session_plenary_ordering_asc_url(api_client, get_or_create_token):
    ORDER_ASC = '?ordering=date'
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    mixer.blend(PlenarySession, date=yesterday)
    mixer.blend(PlenarySession, date=today)
    url = reverse('sessions-list') + ORDER_ASC
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(url)
    respose_json = json.loads(response.content)
    assert response.status_code == 200
    assert respose_json[0]['date'] == yesterday.strftime('%Y-%m-%d')


@pytest.mark.django_db
def test_session_plenary_filter_date_url(api_client, get_or_create_token):
    DATE = '?date={}'
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    mixer.blend(PlenarySession, date=yesterday)
    mixer.blend(PlenarySession, date=today)
    url = reverse('sessions-list') + \
        DATE.format(today.strftime('%Y-%m-%d'))
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(url)
    respose_json = json.loads(response.content)
    assert response.status_code == 200
    assert len(respose_json) == 1
    assert PlenarySession.objects.count() == 2


@pytest.mark.django_db
def test_session_plenary_filter_gte_date_url(api_client, get_or_create_token):
    DATE = '?date__gte={}'
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    mixer.blend(PlenarySession, date=yesterday)
    mixer.blend(PlenarySession, date=today)
    url = reverse('sessions-list') + \
        DATE.format(today.strftime('%Y-%m-%d'))
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(url)
    respose_json = json.loads(response.content)
    assert response.status_code == 200
    assert len(respose_json) == 1
    assert PlenarySession.objects.count() == 2


@pytest.mark.django_db
def test_session_plenary_filter_lte_date_url(api_client, get_or_create_token):
    DATE = '?date__lte={}'
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    mixer.blend(PlenarySession, date=yesterday)
    mixer.blend(PlenarySession, date=today)
    url = reverse('sessions-list') + \
        DATE.format(yesterday.strftime('%Y-%m-%d'))
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(url)
    respose_json = json.loads(response.content)
    assert response.status_code == 200
    assert len(respose_json) == 1
    assert PlenarySession.objects.count() == 2


@pytest.mark.django_db
def test_saved_content_create_db():
    mixer.blend(SavedContent)
    assert SavedContent.objects.count() == 1


@pytest.mark.django_db
def test_saved_content_str():
    content = mixer.blend(SavedContent, title='test title')
    assert content.__str__() == 'test title'


@pytest.mark.django_db
def test_saved_content_create_api(api_client, get_or_create_token):
    session = mixer.blend(PlenarySession)
    data = {
        'content_type': 'tv',
        'title': 'titulo',
        'url': 'http://example.com',
        'session': session.id
    }
    url = reverse('saved-contents-list')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.post(url, data=data)
    request = json.loads(response.content)
    assert response.status_code == 201
    assert request['title'] == 'titulo'
    assert request['content_type'] == 'tv'
    assert request['url'] == 'http://example.com'


@pytest.mark.django_db
def test_unique_saved_content(api_client, get_or_create_token):
    session = mixer.blend(PlenarySession)
    content_type = 'tv'
    title = 'teste'
    url = 'http://teste.com'

    mixer.blend(SavedContent,
                session=session,
                content_type=content_type,
                title=title,
                url=url)
    data = {
        'content_type': content_type,
        'title': title,
        'url': url,
        'session': session.id
    }
    url = reverse('saved-contents-list')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.post(url, data=data)
    request = json.loads(response.content)
    assert response.status_code == 400
    assert request["non_field_errors"] == [
        "Os campos content_type, session, title, url devem criar um set único."
    ]


@pytest.mark.django_db
def test_saved_content_integrity_error():
    content = mixer.blend(SavedContent)
    with pytest.raises(IntegrityError) as excinfo:
        mixer.blend(SavedContent,
                    session=content.session,
                    content_type=content.content_type,
                    title=content.title,
                    url=content.url)
    assert 'duplicate key value violates unique constraint' in str(
        excinfo.value)
