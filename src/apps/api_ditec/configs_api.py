URL = 'http://es-hom.camara.gov.br:9200/{}/_search'
HEADERS = {'Content-Type': 'application/json'}

NUMBER_WEEKS = '4'

DEFAULT_QUERRY = '{"query": {\
                            replace_querry\
                            },\
                    "sort": [\
                        { "dataOrdenacao":   { "order": "desc" }},\
                        { "_score": { "order": "desc" }}\
                    ],\
                    "size": 10,\
                    "from": 0\
                }'


DATE_QUERRY = '"bool": {\
                            "filter": [\
                                {\
                                    "range": {\
                                        "data": {\
                                            "gte": "now-NWw/w"\
                                        }\
                                    }\
                                }\
                            ]\
                        }'

SEARCH_QUERRY = '"match": {"titulo": "words"} '
