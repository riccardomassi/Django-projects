from django.http import HttpResponse
import pytz
from django.utils import timezone
from datetime import datetime
from django.shortcuts import get_object_or_404, render
import logging
from .models import Libro

logger = logging.getLogger(__name__)
MATTONE_THRESHOLD = 300

def hello_template(request):
    # Ottieni l'orario attuale nel fuso orario 'Europe/Rome'
    rome_time = timezone.now().astimezone(pytz.timezone('Europe/Rome'))

    ctx = {"title" : "Hello Template",
           "date" : rome_time}
    
    return render(request, template_name="home.html", context=ctx) 

def lista_libri(request):
    templ = "listalibri.html"

    ctx = { "title": "Lista di Libri", "listalibri": Libro.objects.all()}

    return render(request,template_name=templ,context=ctx)

def mattoni(request):
    templ = "listalibri.html"
    lista_filtrata = Libro.objects.filter(pagine__gte=MATTONE_THRESHOLD) 
    #lista_filtrata = Libro.objects.exclude(pagine__lt=MATTONE_THRESHOLD)
    ctx = { "title":"Lista di Mattoni",
                "listalibri": lista_filtrata}
    
    return render(request,template_name=templ,context=ctx)
    
def autore(request, autore):
    templ = "listalibri.html"
    lista_filtrata = Libro.objects.filter(autore__contains=autore)
    ctx = { "title":"Lista di libri di " + autore,
                "listalibri": lista_filtrata}
    
    return render(request,template_name=templ,context=ctx)

def crea_libro(request):
    message = ""

    if "autore" in request.GET and "titolo" in request.GET:
        aut = request.GET["autore"]
        tit = request.GET["titolo"]
        pag = 100

        try:
            pag = int(request.GET["pagine"])
        except:
            message = "Pagine non valide. Inserite pagine di default."

        l = Libro()
        l.autore = aut
        l.titolo = tit
        l.pagine = pag
        l.data_prestito = datetime.now()

        try:
            l.save()
            message = "Creazione libro riuscita!" + message
        except Exception as e:
            message = "Errore nella creazione del libro " + str(e)

    return render(request, template_name="crealibro.html", 
                  context={"title":"Crea Libro", "message":message})

def modifica_libro(request):
    message = ""
    if request.method == "POST":
        autore = request.POST.get('autore')
        titolo = request.POST.get('titolo')
        nuovo_pagine = request.POST.get('pagine')

        try:
            nuovo_pagine = int(nuovo_pagine)
        except ValueError:
            message = "Pagine non valide. Inserite pagine di default."

        libro = get_object_or_404(Libro, autore=autore, titolo=titolo)
        libro.pagine = nuovo_pagine
        libro.data_prestito = datetime.now()

        try:
            libro.save()
            message = "Modifica libro riuscita!" + message
        except Exception as e:
            message = "Errore nella modifica del libro: " + str(e)

    return render(request, template_name="modificalibro.html", 
                  context={"title": "Modifica Libro", "message": message})

def elimina_libro(request):
    if request.method == "POST":
        titolo_selezionato = request.POST.get('libro_selezionato')
        libro_da_eliminare = get_object_or_404(Libro, titolo=titolo_selezionato)
        libro_da_eliminare.delete()
        message = f"Il libro '{titolo_selezionato}' è stato eliminato con successo."
    else:
        message = ""

    libri = Libro.objects.all()  # Recupera tutti i libri per popolare il menu a tendina
    return render(request, template_name="eliminalibro.html", 
                  context={"title": "Elimina Libro", "message": message, "libri": libri})

