import pytest
from mixer.backend.django import mixer
from datetime import datetime
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.urls import reverse
import json

from .models import PlenarySession, Publication


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
def test_plenary_session_create_erro_user():
    with pytest.raises(Exception):
        mixer.blend(PlenarySession, author=2)


@pytest.mark.django_db
def test_plenary_session_create_erro_location():
    with pytest.raises(Exception):
        plenary_session = mixer.blend(PlenarySession, location='ERROR')
        plenary_session.full_clean()


@pytest.mark.django_db
def test_plenary_session_create_erro_date():
    with pytest.raises(Exception):
        mixer.blend(PlenarySession, date='')


@pytest.mark.django_db
def test_plenary_session_create_erro_type_session():
    with pytest.raises(Exception):
        plenary_session = mixer.blend(PlenarySession, type_session='ERROR')
        plenary_session.full_clean()


@pytest.mark.django_db
def test_plenary_session_create_erro_situation_session():
    with pytest.raises(Exception):
        plenary_session = mixer.blend(PlenarySession,
                                      situation_session='ERROR')
        plenary_session.full_clean()


@pytest.mark.django_db
def test_plenary_session_create_erro_resume():
    with pytest.raises(Exception):
        plenary_session = mixer.blend(PlenarySession, resume='')
        plenary_session.full_clean()


@pytest.mark.django_db
def test_plenary_session_create_none_author():
    with pytest.raises(Exception):
        mixer.blend(PlenarySession, author=None)


@pytest.mark.django_db
def test_plenary_session_create_none_location():
    with pytest.raises(Exception):
        mixer.blend(PlenarySession, location=None)


@pytest.mark.django_db
def test_plenary_session_create_none_date():
    with pytest.raises(Exception):
        mixer.blend(PlenarySession, date=None)


@pytest.mark.django_db
def test_plenary_session_create_none_type_session():
    with pytest.raises(Exception):
        mixer.blend(PlenarySession, type_session=None)


@pytest.mark.django_db
def test_plenary_session_create_none_situation_session():
    with pytest.raises(Exception):
        mixer.blend(PlenarySession,
                    situation_session=None)


@pytest.mark.django_db
def test_plenary_session_create_none_resume():
    with pytest.raises(Exception):
        mixer.blend(PlenarySession, resume=None)


@pytest.mark.django_db
def test_publication_create():
    mixer.blend(Publication)
    assert Publication.objects.count() == 1


@pytest.mark.django_db
def test_publication_str():
    publication = mixer.blend(Publication)
    assert publication.__str__() == '%s' % (
        timezone.now().strftime("%d/%m/%Y, %H:%M:%S"))


@pytest.mark.django_db
def test_publication_create_url(api_client, get_or_create_token):
    session = mixer.blend(PlenarySession)
    data = {
        'content': 'teste',
        'session': session.id
    }
    url = reverse('publications-list')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.post(url, data=data)
    request = json.loads(response.content)
    assert response.status_code == 201
    assert request['content'] == 'teste'
    assert request['state'] == 'published'


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
