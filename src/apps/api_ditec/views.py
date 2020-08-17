from json import JSONDecodeError

import requests
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from rest_framework.response import Response
from rest_framework.views import APIView

from .configs_api import (DEFAULT_QUERY, HEADERS, LAST_UPDATE_QUERY,
                          SEARCH_QUERY)


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


class ListRadioagency(APIView):
    path = '/radioagencia/_search'

    def get(self, request):
        subjects = get_subjects(self.path)
        return Response(subjects)


class SearchRadioagency(APIView):
    path = '/radioagencia/_search'

    def get(self, request, format=None):
        words = request.query_params.get('search', None)
        if words:
            subjects = get_filter_subjects(self.path, words)
        else:
            subjects = {'error': _('It is necessary to pass search')}
        return Response(subjects)


class ListTvCamara(APIView):
    path = '/programas-tv/_search'

    def get(self, request):
        subjects = get_subjects(self.path)
        return Response(subjects)


class SearchTvCamara(APIView):
    path = '/programas-tv/_search'

    def get(self, request, format=None):
        words = request.query_params.get('search', None)
        if words:
            subjects = get_filter_subjects(self.path, words)
        else:
            subjects = {'error': _('It is necessary to pass search')}
        return Response(subjects)


class ListRadioCamara(APIView):
    path = '/programas-radio/_search'

    def get(self, request):
        subjects = get_subjects(self.path)
        return Response(subjects)


class SearchRadioCamara(APIView):
    path = '/programas-radio/_search'

    def get(self, request, format=None):
        words = request.query_params.get('search', None)
        if words:
            subjects = get_filter_subjects(self.path, words)
        else:
            subjects = {'error': _('It is necessary to pass search')}
        return Response(subjects)


def get_subjects(path):
    query = DEFAULT_QUERY.replace('replace_query', LAST_UPDATE_QUERY)

    response = requests.request('POST', settings.API_DITEC + path,
                                headers=HEADERS,
                                data=query)

    try:
        response = response.json()
    except JSONDecodeError:
        response = {'error': _('Error not found results')}

    return response


def get_filter_subjects(path, words):

    query = DEFAULT_QUERY.replace('replace_query', SEARCH_QUERY)
    query = query.replace('words', words)

    response = requests.request('POST', settings.API_DITEC + path,
                                headers=HEADERS,
                                data=query)
    try:
        response = response.json()
    except JSONDecodeError:
        response = {'error': _('Error not found results')}

    return response
