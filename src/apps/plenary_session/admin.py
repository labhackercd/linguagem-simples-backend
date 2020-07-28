from django.contrib import admin
from .models import PlenarySession


class PlenarySessionAdmin(admin.ModelAdmin):
    model = PlenarySession


admin.site.register(PlenarySession, PlenarySessionAdmin)
