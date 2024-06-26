"""
URL configuration for biblio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path 
from .views import *

app_name = "gestione"

urlpatterns = [
    path("listalibri/",lista_libri, name="listalibri"), 
    path('prestito_libro/<int:libro_id>/', prestito_libro, name='prestito_libro'),
    path('esegui_prestito/<int:copia_id>/', esegui_prestito,name='esegui_prestito'),
    path('reso_libro/<int:libro_id>/', reso_libro, name='reso_libro'),
    path('esegui_reso/', esegui_reso, name='esegui_reso'),
    path("mattoni/", mattoni, name="mattoni"),
    path("autore/<str:autore>", autore, name="autore"),
    path("crealibro/", crea_libro, name="crealibro"),
    path("modificalibro/", modifica_libro, name="modificalibro"),
    path("eliminalibro/", elimina_libro, name="eliminalibro"),
]
