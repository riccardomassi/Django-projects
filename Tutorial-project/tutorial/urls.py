"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from views import home_page, elenca_params, hello_template

#lista di percorsi raggiungibili 
urlpatterns = [
    path('admin/', admin.site.urls),           #tt quelli necessari per i percorsi di amministrazione
    #path("home/", home_page, name="homepage"), #path relativo home per dare homepage all'app
    re_path(r"^$|^/$|^home/$", home_page, name="homepage"),
    #path("elencoparametri/", elenca_params,name="params")
    path("hellotemplate/",hello_template, name="hellotemplate")
    
]

#posso arrivare all'hompage di un sito da diverse strade --> no url univoco --> diversi indirizzi che puntano allo stesso punto terminale
#che va a chimare la fun vista prima = 
# Una prima soluzione: 
# path("/", home_page, name="homepage"),
# path("", home_page, name="homepage")
# questa però è una soluzione poco elegante e macchinosa --> regex
# re_path(r"^$"|^/$|^home/$", home_page, name="homepage")
