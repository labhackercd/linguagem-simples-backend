import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .configs_api import (DEFAULT_QUERRY, DATE_QUERRY, SEARCH_QUERRY,
                          NUMBER_WEEKS, URL, HEADERS)


class ListNews(APIView):

    def get(self, request):
        news = self.get_news()
        return Response(news)

    def get_news(self):
        url_prefix = 'noticias'
        querry = DEFAULT_QUERRY.replace('replace_querry', DATE_QUERRY)
        querry = querry.replace('NW', NUMBER_WEEKS)

        response = requests.request('POST', URL.format(url_prefix),
                                    headers=HEADERS,
                                    data=querry)
        try:
            response = response.json()
        except Exception:
            response = {'error': 'Error not found news'}

        return response


class SearchNews(APIView):

    def get(self, request, format=None):
        words = request.query_params.get('search', None)
        if words:
            news = self.get_filter_news(words)
        else:
            news = {'error': 'It is necessary to pass search'}
        return Response(news)

    def get_filter_news(self, words):
        url_prefix = 'noticias'

        querry = DEFAULT_QUERRY.replace('replace_querry', SEARCH_QUERRY)
        querry = querry.replace('words', words)

        response = requests.request('POST', URL.format(url_prefix),
                                    headers=HEADERS,
                                    data=querry)
        try:
            response = response.json()
        except Exception:
            response = {'error': 'Error not found news'}

        return response
