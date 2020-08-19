from json import JSONDecodeError

import requests
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from rest_framework.response import Response
from rest_framework.views import APIView

from .configs_api import (DEFAULT_QUERY, HEADERS, LAST_UPDATE_QUERY,
                          SEARCH_QUERY, PATH_PROGRAMA_TV, PATH_NOTICIAS,
                          PATH_PROGRAMA_RADIO, PATH_RADIOAGENCIA)


class ListNews(APIView):
    def get(self, request):
        subjects = get_subjects(PATH_NOTICIAS)
        return Response(subjects)


class SearchNews(APIView):
    def get(self, request, format=None):
        words = request.query_params.get('search', None)
        subjects = get_filter_subjects(words, PATH_NOTICIAS)
        return Response(subjects)


class ListRadioagency(APIView):
    def get(self, request):
        subjects = get_subjects(PATH_RADIOAGENCIA)
        return Response(subjects)


class SearchRadioagency(APIView):
    def get(self, request, format=None):
        words = request.query_params.get('search', None)
        subjects = get_filter_subjects(words, PATH_RADIOAGENCIA)
        return Response(subjects)


class ListTvCamara(APIView):
    def get(self, request):
        subjects = get_subjects(PATH_PROGRAMA_TV)
        return Response(subjects)


class SearchTvCamara(APIView):
    def get(self, request, format=None):
        words = request.query_params.get('search', None)
        subjects = get_filter_subjects(words, PATH_PROGRAMA_TV)
        return Response(subjects)


class ListRadioCamara(APIView):
    def get(self, request):
        subjects = get_subjects(PATH_PROGRAMA_RADIO)
        return Response(subjects)


class SearchRadioCamara(APIView):
    def get(self, request, format=None):
        words = request.query_params.get('search', None)
        subjects = get_filter_subjects(words, PATH_PROGRAMA_RADIO)
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


def get_filter_subjects(words, path):
    if words:
        query = DEFAULT_QUERY.replace('replace_query', SEARCH_QUERY)
        query = query.replace('words', words)

        response = requests.request('POST', settings.API_DITEC + path,
                                    headers=HEADERS,
                                    data=query)
        try:
            response = response.json()
        except JSONDecodeError:
            response = {'error': _('Error not found results')}
    else:
        response = {'error': _('It is necessary to pass search')}

    return response
