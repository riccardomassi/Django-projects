from django.urls import path
from .views import search, IndexViewList, ChoiceView, SearchResultsList

app_name = "polls"

urlpatterns = [
  path('', IndexViewList.as_view(), name='index'),
  path('<pk>/detail/', ChoiceView.as_view(), name='detail'),
  path("search/", search, name="search"),
  path("searchresults/<str:sstring>/<str:where>/", SearchResultsList.as_view(), name="searchresults")
]

