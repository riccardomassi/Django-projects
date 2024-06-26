from django.urls import path
from .views import *

app_name = 'iscrizioni'

urlpatterns = [
  path("listastudenti/", ListaStudentiView.as_view(), name = "listastudenti"),
  path("listainsegnamenti/", ListaInsegnamentiView.as_view(), name = "listainsegnamenti"),
  path("insegnamentiattivi/", ListaInsegnamentiAttivi.as_view(), name = "insegnamentiattivi"),
  path("numeroiscrizioni/", NumeroIscrizioniView.as_view(), name = "numeroiscrizioni"),
  path("creastudente/", CreateStudenteView.as_view(),name="creastudente"),
  path("creainsegnamento/", CreateInsegnamentoView.as_view(),name="creainsegnamento"),
  path("insegnamento/<pk>/", DetailInsegnamentoView.as_view(), name="insegnamento"),
  path("modificainsegnamento/<pk>/", UpdateInsegnamentoView.as_view(), name="modificainsegnamento"),
  path("eliminainsegnamento/<pk>/", DeleteInsegnamentoView.as_view(), name="eliminainsegnamento"),
  path("eliminastudente/<pk>/", DeleteStudenteView.as_view(), name="eliminastudente"),
  path("cercastudenti/", CercaStudentiView.as_view(), name="cercastudenti"),
]
