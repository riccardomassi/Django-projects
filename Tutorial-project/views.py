#guarda che cos è la richiesta http e  il  protocollo http (protocolli di rete) + richieste GET 
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def elenca_params(request):
    
    response = ""
    for k in request.GET:
        request += request.GET[k] + ""
        
    return HttpResponse(response) 

def hello_template(request):
    ctx = { "title" : "Hello Template",
           "lista" : [datetime.now(), datetime.today().strftime('%A'),  datetime.today().strftime('%B')]}
    
    return render(request, template_name="baseext.html", context=ctx)
        
    

def home_page(request): #fun che dettagli la business logic dell'app --> tt ciò che riguarda la business logic è in views.py
    #codice del mio server--> interpreta tt e comporrà un oggetto 
    #risorsa generalta al volo (web dinamico) come codice arbitrario
    
    #response = "Benvenuto nella Homepage, " + str(request.user)
    #non va a capo (senza <div>) pk interpretato in formato html --> ho bisogno dei template 
    response = "ciao, <br> sono andato a capo"
    
    """
    
    print("RESPONSE: " + str(request))
    print("Caratteristiche di request" + str(dir(request)))
    
    for e in request.__dict__:
        print(e)
    print("USER " + str(request.user))
    print("PATH ") + str(request.path)
    
    """
    if not request.user.is_authenticated:
        logger.warning(str(request.user) + " non è autenticato!")

    return HttpResponse(response) 
