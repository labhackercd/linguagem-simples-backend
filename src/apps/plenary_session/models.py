from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import Q


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

    location = models.CharField(verbose_name=_('location'), max_length=20,
                                choices=list_location)
    date = models.DateField(verbose_name=_('date'))
    type_session = models.CharField(verbose_name=_('type_session'),
                                    max_length=20,
                                    choices=list_type_session)
    situation_session = models.CharField(verbose_name=_('situation_session'),
                                         max_length=20,
                                         choices=list_situation_session)
    resume = models.TextField(verbose_name=_('resume'), blank=True, default='')

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
    session = models.ForeignKey('plenary_session.PlenarySession',
                                on_delete=models.CASCADE,
                                related_name="publications",
                                verbose_name=_('plenary session'))
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.PROTECT,
                               related_name="publications",
                               verbose_name=_('author'))
    content = models.TextField(_('content'), null=True, blank=True)
    tweet_id = models.CharField(max_length=200,
                                verbose_name=_('tweet id'),
                                null=True, blank=True)
    image = models.ImageField(upload_to='uploads/',
                              verbose_name=_('image'),
                              null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~Q(content__exact='')
                | Q(tweet_id__isnull=False)
                | ~Q(image__exact=''),
                name='not_content_tweet_image_null'
            )
        ]
        verbose_name = _('publication')
        verbose_name_plural = _('publications')

    def clean(self):
        super().clean()
        if (bool(self.content) is False and
            self.tweet_id is None and
                bool(self.image) is False):
            raise ValidationError(
                _('Content or tweet_id or image are required'))

    def __str__(self):
        return self.created.strftime("%d/%m/%Y, %H:%M:%S")


class SavedContent(TimestampedMixin):
    TYPE_CHOICES = (
        ('news', _('News')),
        ('tv', _('TV Câmara')),
        ('radio', _('Radio Câmara')),
        ('agency', _('Agencia Câmara')),
    )

    content_type = models.CharField(verbose_name=_('state'),
                                    choices=TYPE_CHOICES,
                                    max_length=120,
                                    default='published')
    session = models.ForeignKey('plenary_session.PlenarySession',
                                on_delete=models.CASCADE,
                                related_name="saved_contents",
                                verbose_name=_('saved content'))
    title = models.CharField(max_length=200, verbose_name=_('title'))
    url = models.URLField(verbose_name=_('url'))

    class Meta:
        verbose_name = _('saved content')
        verbose_name_plural = _('saved contents')
        unique_together = ('content_type', 'session', 'title', 'url')

    def __str__(self):
        return self.title
