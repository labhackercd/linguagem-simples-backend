import pytest
from mixer.backend.django import mixer

from .models import PlenarySession


@pytest.mark.django_db
def test_apps():
    from apps.plenary_session.apps import PlenarySessionConfig
    assert PlenarySessionConfig.name == 'plenary_session'


@pytest.mark.django_db
def test_plenary_session_create():
    mixer.blend(PlenarySession)
    assert PlenarySession.objects.count() == 1


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
