from django.contrib.auth import get_user_model
from django.urls import reverse


import pytest
from unittest import mock

from .views import get_news, get_filter_news


@pytest.mark.django_db
@mock.patch('apps.api_ditec.views.requests.request')
def test_get_news(mock_request):
    mock_request.return_value.ok = True

    response = get_news()
    assert response.data['id']
    assert response


@pytest.mark.django_db
@mock.patch('apps.api_ditec.views.requests.request')
def test_get_filter_news(mock_request):
    mock_request.return_value.ok = True

    response = get_filter_news('words')
    assert response.data['id']
    assert response
