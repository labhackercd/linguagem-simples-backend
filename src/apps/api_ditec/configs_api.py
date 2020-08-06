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
