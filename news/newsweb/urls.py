from django.urls import path

from . import views

# Creation of all of the URL patterns, their extensions, and functionalities
urlpatterns = [
    path('technology', views.technology),
    path('techsearchresults', views.searchTechnology),
    path('sports', views.sports),
    path('sportssearchresults', views.searchSports),
    path('entertainment', views.entertainment),
    path('entertainmentsearchresults', views.searchEntertainment),
    path('topinUS', views.home),
    path('USsearchresults', views.searchTopUS),
    path('', views.titlepage)

]
