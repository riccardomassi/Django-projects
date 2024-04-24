from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import *
from django.shortcuts import render

class ListaStudentiView(ListView):
  model = Studente
  template_name = "iscrizioni/lista_studenti.html"

class ListaInsegnamentiView(ListView):
    model = Insegnamento
    template_name = 'iscrizioni/lista_insegnamenti.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        insegnamenti = context['object_list']
        for insegnamento in insegnamenti:
            insegnamento.studenti_list = insegnamento.studenti.all()
        return context
    
class ListaInsegnamentiAttivi(ListView):
  model = Insegnamento
  template_name = "iscrizioni/insegnamenti_attivi.html"

  def get_queryset(self):
    return self.model.objects.exclude(studenti__isnull=True)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titolo'] = "Insegnamenti Attivi"
    return context
  
class NumeroIscrizioniView(ListView):
  model = Studente
  template_name = "iscrizioni/numero_iscrizioni.html"

  def get_model_name(self):
    return self.model._meta.verbose_name_plural
  
  def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx["titolo"] = "Lista Studenti con Iscrizioni"
    return ctx

  def get_totale_iscrizioni(self):
    count = 0
    for i in Insegnamento.objects.all():
       count += i.studenti.all().count()
    return count 

class CreateStudenteView(CreateView):
  model = Studente
  template_name = "iscrizioni/crea_studente.html"
  fields = "__all__"
  success_url = reverse_lazy("iscrizioni:listastudenti")  

class CreateInsegnamentoView(CreateView):
  model = Insegnamento
  template_name = "iscrizioni/crea_insegnamento.html"
  fields = "__all__"
  success_url = reverse_lazy("iscrizioni:listainsegnamenti")

class DetailInsegnamentoView(DetailView):
  model = Insegnamento
  template_name = "iscrizioni/insegnamento.html"

class UpdateInsegnamentoView(UpdateView):
  model = Insegnamento
  template_name = "iscrizioni/modifica_insegnamento.html"
  fields = "__all__"
  
  def get_success_url(self):
    return reverse_lazy("iscrizioni:insegnamento", kwargs={"pk": self.object.pk})
  
class DeleteEntitaView(DeleteView):
  template_name = "iscrizioni/elimina_entita.html"

  def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    entita = "Studente"
    if self.model == Insegnamento:
      entita = "Insegnamento"
    ctx["entita"] = entita
    ctx["name"] = self.get_object()
    return ctx
  
  def get_success_url(self): 
    if self.model == Studente:
      return reverse_lazy("iscrizioni:listastudenti")
    else: 
      reverse_lazy("iscrizioni:listainsegnamenti")

class DeleteStudenteView(DeleteEntitaView):
  model = Studente

class DeleteInsegnamentoView(DeleteEntitaView):
  model = Insegnamento


class CercaStudentiView(ListView):
  model = Studente
  template_name = "iscrizioni/cerca_studenti.html"

  def post(self, request):
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    studenti = self.model.objects.filter(name__icontains=name, surname__icontains=surname)
    insegnamenti = Insegnamento.objects.filter(studenti__in=studenti)
    context = {
      'studenti': studenti,
      'insegnamenti': insegnamenti
    }
    return render(request, self.template_name, context)
  
