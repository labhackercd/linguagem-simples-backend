PATH_PROGRAMA_RADIO = '/programas-radio/_search'
PATH_PROGRAMA_TV = '/programas-tv/_search'
PATH_RADIOAGENCIA = '/radioagencia/_search'
PATH_NOTICIAS = '/noticias/_search'


HEADERS = {'Content-Type': 'application/json'}

DEFAULT_QUERY = '{"query": {\
                            replace_query\
                            },\
                    "sort": [\
                        { "dataOrdenacao":   { "order": "desc" }},\
                        { "_score": { "order": "desc" }}\
                    ],\
                    "size": 50,\
                    "from": 0\
                }'


LAST_UPDATE_QUERY = '"match_all" : {} '

SEARCH_QUERY = '"match": {"titulo": "words"} '
