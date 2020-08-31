from django.contrib import admin

from .models import PlenarySession, Publication, SavedContent


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
        'title',
    )
    list_filter = ('created', 'modified', 'session', 'author')


@admin.register(SavedContent)
class SavedContentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'content_type',
        'session',
        'title',
        'url',
    )
    list_filter = ('created', 'modified', 'session')
