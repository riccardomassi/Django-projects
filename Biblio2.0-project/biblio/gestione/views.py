from django.shortcuts import render, redirect
from django.views.generic import ListView
from django import forms
from .models import Libro
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.views.generic import ListView
from .models import Libro

def gestione_home(request):
  return render(request,template_name="gestione/home.html")

class LibroListView(ListView):
  titolo = "La nostra biblioteca possiede" 
  model = Libro
  template_name = "gestione/lista_libri.html"

class SearchForm(forms.Form):
    CHOICE_LIST = [("Titolo","Cerca tra i titoli"), ("Autore","Cerca tra gli autori")]
    helper = FormHelper()
    helper.form_id = "search_crispy_form"
    helper.form_method = "POST"
    helper.add_input(Submit("submit","Cerca"))
    search_string = forms.CharField(label="Cerca qualcosa",max_length=100,min_length=3, required=True)
    search_where = forms.ChoiceField(label="Dove?", required=True, choices=CHOICE_LIST)

def search(request):
  if request.method == "POST":
    form = SearchForm(request.POST) 
    if form.is_valid():
      sstring = form.cleaned_data.get("search_string")
      where = form.cleaned_data.get("search_where")
      return redirect("gestione:ricerca_risultati", sstring, where)
  else:
    form = SearchForm()
    return render(request,template_name="gestione/ricerca.html",context={"form":form}) 

class LibroRicercaView(LibroListView):
  titolo = "La tua ricerca ha dato come risultato"

  def get_queryset(self):
    sstring = self.request.resolver_match.kwargs["sstring"] 
    where = self.request.resolver_match.kwargs["where"]

    if "Titolo" in where:
      qq = self.model.objects.filter(titolo__icontains=sstring)
    else:
      qq = self.model.objects.filter(autore__icontains=sstring)
    return qq
