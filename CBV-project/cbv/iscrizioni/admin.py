from django.contrib import admin
from .models import Studente, Insegnamento, Iscrizione

admin.site.register(Studente)
admin.site.register(Insegnamento)
admin.site.register(Iscrizione)
