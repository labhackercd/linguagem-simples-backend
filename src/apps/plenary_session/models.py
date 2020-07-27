from django.db import models


class PlenarySession(models.Model):
    list_location = [('PLENARIO', 'Plenário')]
    list_type_session = [('VIRTUAL', 'Sessão Virtual'),
                         ('PRESENCIAL', 'Sessão Precensial')
                         ]
    list_situation_session = [('PRE_SESSAO', 'Pré-Sessão'),
                              ('SESSAO_INICIADA', 'Sessão Iniciada'),
                              ('VOTACAO_INICIADA', 'Votação Iniciada'),
                              ('PROXIMA_PAUTA', 'Próxima Pauta'),
                              ('SESSAO_ENCERRADA', 'Sessão Encerrada'),
                              ]

    location = models.CharField(max_length=20, choices=list_location)
    date = models.DateField()
    type_session = models.CharField(max_length=20, choices=list_type_session)
    situation_session = models.CharField(max_length=20,
                                         choices=list_situation_session)
    resume = models.TextField()
