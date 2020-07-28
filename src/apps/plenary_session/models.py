from django.db import models
from django.utils.translation import gettext_lazy as _


class PlenarySession(models.Model):
    list_location = [('plenary', _('plenary'))]
    list_type_session = [('virtual', _('virtual session')),
                         ('presential', _('presential session'))
                         ]
    list_situation_session = [('pre_session', _('pré session')),
                              ('started_session', _('started session')),
                              ('started_votation', _('started votation')),
                              ('next_topic', _('next topic')),
                              ('closed_session', _('closed session')),
                              ]

    location = models.CharField(max_length=20, choices=list_location)
    date = models.DateField()
    type_session = models.CharField(max_length=20, choices=list_type_session)
    situation_session = models.CharField(max_length=20,
                                         choices=list_situation_session)
    resume = models.TextField()

    class Meta:
        verbose_name = _('plenary session')
        verbose_name_plural = _('plenary sessions')

    def __str__(self):
        return (self.type_session + ' - ' + self.date.strftime("%d/%m/%Y"))
