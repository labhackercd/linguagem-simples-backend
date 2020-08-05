HEADERS = {'Content-Type': 'application/json'}

NUMBER_WEEKS = '4'

DEFAULT_QUERY = '{"query": {\
                            replace_query\
                            },\
                    "sort": [\
                        { "dataOrdenacao":   { "order": "desc" }},\
                        { "_score": { "order": "desc" }}\
                    ],\
                    "size": 10,\
                    "from": 0\
                }'


DATE_QUERY = '"bool": {\
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

SEARCH_QUERY = '"match": {"titulo": "words"} '
