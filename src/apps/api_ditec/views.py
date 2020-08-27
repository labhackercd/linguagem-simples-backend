from json import JSONDecodeError
from typing import Dict
import requests
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from linguagemsimples.utils.scrape import Scrape


from .configs_api import (DEFAULT_QUERY, HEADERS, LAST_UPDATE_QUERY,
                          SEARCH_QUERY, PATH_PROGRAMA_TV, PATH_NOTICIAS,
                          PATH_PROGRAMA_RADIO, PATH_RADIOAGENCIA)


DictResponse = Dict[str, str]


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


def get_subjects(path: str) -> DictResponse:
    query = DEFAULT_QUERY.replace('replace_query', LAST_UPDATE_QUERY)

    response = requests.request('POST', settings.API_DITEC + path,
                                headers=HEADERS,
                                data=query)

    try:
        response = response.json()
    except JSONDecodeError:
        response = {'error': _('Error not found results')}

    return response


def get_filter_subjects(words: str, path: str) -> DictResponse:
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


class VideosSession(APIView):
    @swagger_auto_schema(operation_description="Get videos from session. It's \
                         necessary to pass 'id_video' by session ",
                         responses={200: "{'1': {'url': '...',\
                                                 'decription': '...',\
                                                 'thumbnail': '...'}}",
                                    404: 'Videos sessions not found!'})
    def get(self, request, id_video, format=None):
        scrape = Scrape()
        page = scrape.get_webpage_videos(id_video)
        if page.status_code == 200:
            videos_json = scrape.scraping_videos(page.text)
        else:
            videos_json = {'error': _('Videos sessions not found!')}
        return JsonResponse(videos_json, safe=False)
