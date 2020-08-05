import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .configs_api import (DEFAULT_QUERY, DATE_QUERY, SEARCH_QUERY,
                          NUMBER_WEEKS, HEADERS)
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class ListNews(APIView):

    def get(self, request):
        news = self.get_news()
        return Response(news)

    def get_news(self):
        path = '/noticias/_search'
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


class SearchNews(APIView):

    def get(self, request, format=None):
        words = request.query_params.get('search', None)
        if words:
            news = self.get_filter_news(words)
        else:
            news = {'error': _('It is necessary to pass search')}
        return Response(news)

    def get_filter_news(self, words):
        path = '/noticias/_search'

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
