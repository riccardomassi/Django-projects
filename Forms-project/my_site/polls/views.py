from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView

from .forms import SearchForm
from .models import Question

class IndexViewList(ListView): 
  model = Question
  template_name = 'polls/index.html' 

  def get_queryset(self):
    return self.model.objects.order_by('-pub_date')[:20]
  
class ChoiceView(DetailView):
  model = Question
  template_name = 'polls/detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['choices'] = self.object.choices.all()
    return context 
  
def search(request):
  if request.method == "POST":
    form = SearchForm(request.POST) 
    if form.is_valid():
      sstring = form.cleaned_data.get("search_string")
      where = form.cleaned_data.get("search_where")
      return redirect("polls:searchresults", sstring, where)
  else:
    form = SearchForm()
    
  return render(request,template_name="polls/searchpage.html",context={"form":form})

class SearchResultsList(ListView):
  model = Question
  template_name = 'polls/searchresults.html'

  def get_queryset(self):
    sstring = self.kwargs.get("sstring")
    where = self.kwargs.get("where")
    if where == "Questions":
      return self.model.objects.filter(question_text__icontains=sstring)
    else:
      return self.model.objects.filter(choices__choice_text__icontains=sstring)
    

  
  



  

  

