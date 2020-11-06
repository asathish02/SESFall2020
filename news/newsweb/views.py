from django.shortcuts import render
from .forms import SearchFunction
from django.http import HttpResponse

# Create your views here.
def home(request):
    import requests
    import json

    # Returns the top headlines in the US on the home page
    link_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=78b9d599c4f94f8fa3afb1a5458928d6"
    news_api_request = requests.get(link_url)

    api = json.loads(news_api_request.content)
    return render(request, 'home.html', {'api': api})


def sports(request):
    import requests
    import json

    # Returns the top headlines in the US on the home page
    link_url = "http://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=78b9d599c4f94f8fa3afb1a5458928d6"
    news_api_request = requests.get(link_url)

    api = json.loads(news_api_request.content)
    return render(request, 'sports.html', {'api': api})


def entertainment(request):
    import requests
    import json

    # Returns the top headlines in the US on the home page
    link_url = \
        "http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=78b9d599c4f94f8fa3afb1a5458928d6"
    news_api_request = requests.get(link_url)

    api = json.loads(news_api_request.content)
    return render(request, 'entertainment.html', {'api': api})


def technology(request):
    import requests
    import json

    # Returns the top headlines in the US on the home page
    link_url = \
        "http://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=78b9d599c4f94f8fa3afb1a5458928d6"
    news_api_request = requests.get(link_url)

    api = json.loads(news_api_request.content)
    return render(request, 'technology.html', {'api': api})


def titlepage(request):
    return render(request, 'TitlePage.html')


def searchTechnology(request):
    import requests
    import json

    keyword = request.POST.get('mytextbox')

    new_link_url = "http://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=78b9d599c4f94f8fa3afb1a5458928d6" +"&q=" + keyword
    news_api_request = requests.get(new_link_url)
    api = json.loads(news_api_request.content)

    return render(request, 'techsearchresults.html', {'api': api})

def searchSports(request):
    import requests
    import json

    keyword = request.POST.get('mytextbox')

    new_link_url = "http://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=78b9d599c4f94f8fa3afb1a5458928d6" +"&q=" + keyword
    news_api_request = requests.get(new_link_url)
    api = json.loads(news_api_request.content)

    return render(request, 'sportssearchresults.html', {'api': api})

def searchEntertainment(request):
    import requests
    import json

    keyword = request.POST.get('mytextbox')

    new_link_url = "http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=78b9d599c4f94f8fa3afb1a5458928d6" +"&q=" + keyword
    news_api_request = requests.get(new_link_url)
    api = json.loads(news_api_request.content)

    return render(request, 'entertainmentsearchresults.html', {'api': api})

def searchTopUS(request):
    import requests
    import json

    keyword = request.POST.get('mytextbox')

    new_link_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=78b9d599c4f94f8fa3afb1a5458928d6" +"&q=" + keyword
    news_api_request = requests.get(new_link_url)
    api = json.loads(news_api_request.content)

    return render(request, 'USsearchresults.html', {'api': api})