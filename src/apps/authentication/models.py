from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    PROFILE_CHOICES = (
        ('editor', _('editor')),
    )
    email = models.EmailField(_('email address'), unique=True)
    profile = models.CharField(choices=PROFILE_CHOICES, max_length=120,
                               default='editor')
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username
