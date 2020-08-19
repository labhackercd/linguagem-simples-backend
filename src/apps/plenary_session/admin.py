from django.contrib import admin

from .models import PlenarySession, Publication


@admin.register(PlenarySession)
class PlenarySessionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'author',
        'location',
        'date',
        'type_session',
        'situation_session',
        'resume',
    )
    list_filter = ('created', 'modified', 'author', 'date')


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'state',
        'session',
        'author',
        'content',
        'tweet_id',
        'image',
    )
    list_filter = ('created', 'modified', 'session', 'author')
