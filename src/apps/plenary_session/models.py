from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class TimestampedMixin(models.Model):
    created = models.DateTimeField(_('created'), editable=False,
                                   blank=True, auto_now_add=True)
    modified = models.DateTimeField(_('modified'), editable=False,
                                    blank=True, auto_now=True)

    class Meta:
        abstract = True


class PlenarySession(TimestampedMixin):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="plenary_sessions"
    )
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


class Publication(TimestampedMixin):
    STATE_CHOICES = (
        ('published', _('published')),
        ('inactive', _('inactive')),
    )

    state = models.CharField(verbose_name=_('state'),
                             choices=STATE_CHOICES,
                             max_length=120,
                             default='published')
    content = models.TextField(_('content'))
    session = models.ForeignKey('plenary_session.PlenarySession',
                                on_delete=models.CASCADE,
                                related_name="publications",
                                verbose_name=_('plenary session'))
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.PROTECT,
                               related_name="publications",
                               verbose_name=_('author'))

    class Meta:
        verbose_name = _('publication')
        verbose_name_plural = _('publications')

    def __str__(self):
        return self.created.strftime("%d/%m/%Y, %H:%M:%S")
