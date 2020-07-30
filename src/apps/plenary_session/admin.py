from django.contrib import admin

from .models import PlenarySession, Publication


@admin.register(PlenarySession)
class PlenarySessionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'location',
        'date',
        'type_session',
        'situation_session',
        'resume',
    )
    list_filter = ('author', 'date')


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'state',
        'content',
        'session',
        'author',
    )
    list_filter = ('created', 'modified', 'session', 'author')
