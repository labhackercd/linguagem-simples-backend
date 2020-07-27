from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

# Create your tests here.
import pytest

from .models import PlenarySession
from datetime import datetime


@pytest.mark.django_db
def test_plenary_session_create():
    PlenarySession.objects.create(location='PLENARIO',
                                  date=datetime.now(),
                                  type_session='VIRTUAL',
                                  situation_session='PRE_SESSAO',
                                  resume="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    assert PlenarySession.objects.count() == 1


@pytest.mark.django_db
def test_plenary_session_create_erro_location():
    with pytest.raises(ValidationError):
        plenary_session = PlenarySession.objects.create(location='ERROR',
                                                        date=datetime.now(),
                                                        type_session='VIRTUAL',
                                                        situation_session='PRE_SESSAO',
                                                        resume="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

        plenary_session.full_clean()


@pytest.mark.django_db
def test_plenary_session_create_erro_date():
    with pytest.raises(ValidationError):
        plenary_session = PlenarySession.objects.create(location='PLENARIO',
                                                        date='',
                                                        type_session='VIRTUAL',
                                                        situation_session='PRE_SESSAO',
                                                        resume="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

        plenary_session.full_clean()


@pytest.mark.django_db
def test_plenary_session_create_erro_type_session():
    with pytest.raises(ValidationError):
        plenary_session = PlenarySession.objects.create(location='PLENARIO',
                                                        date=datetime.now(),
                                                        type_session='ERROR',
                                                        situation_session='PRE_SESSAO',
                                                        resume="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

        plenary_session.full_clean()


@pytest.mark.django_db
def test_plenary_session_create_erro_situation_session():
    with pytest.raises(ValidationError):
        plenary_session = PlenarySession.objects.create(location='PLENARIO',
                                                        date=datetime.now(),
                                                        type_session='VIRTUAL',
                                                        situation_session='ERROR',
                                                        resume="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

        plenary_session.full_clean()


@pytest.mark.django_db
def test_plenary_session_create_erro_resume():
    with pytest.raises(ValidationError):
        plenary_session = PlenarySession.objects.create(location='PLENARIO',
                                                        date=datetime.now(),
                                                        type_session='VIRTUAL',
                                                        situation_session='PRE_SESSAO',
                                                        )

        plenary_session.full_clean()
