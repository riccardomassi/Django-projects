#guarda che cos è la richiesta http e  il  protocollo http (protocolli di rete) + richieste GET 
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
import logging
from .models import Libro

logger = logging.getLogger(__name__)

def hello_template(request):
    ctx = { "title" : "Hello Template",
           "lista" : [datetime.now(), datetime.today().strftime('%A'),  datetime.today().strftime('%B')]}
    
    return render(request, template_name="baseext.html", context=ctx) 

def lista_libri(request):
    templ = "listalibri.html"

    ctx = { "title": "Lista di Libri", "listalibri": Libro.objects.all()}

    return render(request,template_name=templ,context=ctx)

