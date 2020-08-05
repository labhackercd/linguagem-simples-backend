import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .configs_api import (DEFAULT_QUERY, DATE_QUERY, SEARCH_QUERY,
                          NUMBER_WEEKS, HEADERS)
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class ListNews(APIView):
    path = '/noticias/_search'

    def get(self, request):
        subjects = get_subjects(self.path)
        return Response(subjects)


class SearchNews(APIView):
    path = '/noticias/_search'

    def get(self, request, format=None):
        words = request.query_params.get('search', None)
        if words:
            subjects = get_filter_subjects(self.path, words)
        else:
            subjects = {'error': _('It is necessary to pass search')}
        return Response(subjects)


def get_subjects(path):
    query = DEFAULT_QUERY.replace('replace_query', DATE_QUERY)
    query = query.replace('NW', NUMBER_WEEKS)

    response = requests.request('POST', settings.API_DITEC + path,
                                headers=HEADERS,
                                data=query)
    try:
        response = response.json()
    except Exception:
        response = {'error': _('Error not found news')}

    return response


def get_filter_subjects(path, words):

    query = DEFAULT_QUERY.replace('replace_query', SEARCH_QUERY)
    query = query.replace('words', words)

    response = requests.request('POST', settings.API_DITEC + path,
                                headers=HEADERS,
                                data=query)
    try:
        response = response.json()
    except Exception:
        response = {'error': _('Error not found news')}

    return response
