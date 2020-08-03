import requests
from rest_framework.views import APIView
from rest_framework.response import Response

URL = "http://es-hom.camara.gov.br:9200/{}/_search"

NUMBER_WEEKS = 4

DATE_QUERRY = '{\
                    "query": {\
                        "bool": {\
                            "filter": [\
                                {\
                                    "range": {\
                                        "data": {\
                                            "gte": "now-%dw/w"\
                                        }\
                                    }\
                                }\
                            ]\
                        }\
                    },\
                    "sort": [\
                        { "dataOrdenacao":   { "order": "desc" }},\
                        { "_score": { "order": "desc" }}\
                    ],\
                    "size": 10,\
                    "from": 0\
                }'
headers = {'Content-Type': 'application/json'}


class ListNews(APIView):

    def get(self, request, format=None):
        news = self.get_news()
        return Response(news)

    def get_news(self):
        url_prefix = 'noticias'
        querry = DATE_QUERRY.replace("%d", NUMBER_WEEKS)

        response = requests.request("POST", URL.format(url_prefix),
                                    headers=headers,
                                    data=querry)
        try:
            response.json()
        except Exception:
            response = {"error": "Error not found news"}

        return response


