from django.shortcuts import render


# Function for constructing TopinUS tab
def home(request):
    import requests
    import json

    # Returns the top headlines in the US on the page
    link_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=78b9d599c4f94f8fa3afb1a5458928d6"
    news_api_request = requests.get(link_url)

    api = json.loads(news_api_request.content)
    return render(request, 'home.html', {'api': api})


# Function for constructing sports tab
def sports(request):
    import requests
    import json

    # Returns the top headlines in the US with the sports category
    link_url = "http://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=78b9d599c4f94f8fa3afb1a5458928d6"
    news_api_request = requests.get(link_url)

    api = json.loads(news_api_request.content)
    return render(request, 'sports.html', {'api': api})


# Function for constructing entertainment tab
def entertainment(request):
    import requests
    import json

    # Returns the top headlines in the US with the entertainment category
    link_url = \
        "http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=78b9d599c4f94f8fa3afb1a5458928d6"
    news_api_request = requests.get(link_url)

    api = json.loads(news_api_request.content)
    return render(request, 'entertainment.html', {'api': api})


# Function for constructing technology tab
def technology(request):
    import requests
    import json

    # Returns the top headlines in the US with the technology category
    link_url = \
        "http://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=78b9d599c4f94f8fa3afb1a5458928d6"
    news_api_request = requests.get(link_url)

    api = json.loads(news_api_request.content)
    return render(request, 'technology.html', {'api': api})


# Function for constructing TitlePage tab
def titlepage(request):
    return render(request, 'TitlePage.html')


# Function for constructing technology search results tab
def searchTechnology(request):
    import requests
    import json

    # Store input from input box to variable
    keyword = request.POST.get('mytextbox')

    # Append the keyword to the URL and load search results page with this parameter
    new_link_url = "http://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=78b9d599c4f94f8fa3afb1a5458928d6" + "&q=" + keyword
    news_api_request = requests.get(new_link_url)
    api = json.loads(news_api_request.content)

    return render(request, 'techsearchresults.html', {'api': api})


# Function for constructing sports search results tab
def searchSports(request):
    import requests
    import json

    # Store input from input box to variable
    keyword = request.POST.get('mytextbox')

    # Append the keyword to the URL and load search results page with this parameter
    new_link_url = "http://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=78b9d599c4f94f8fa3afb1a5458928d6" + "&q=" + keyword
    news_api_request = requests.get(new_link_url)
    api = json.loads(news_api_request.content)

    return render(request, 'sportssearchresults.html', {'api': api})


# Function for constructing entertainment search results tab
def searchEntertainment(request):
    import requests
    import json

    # Store input from input box to variable
    keyword = request.POST.get('mytextbox')

    # Append the keyword to the URL and load search results page with this parameter
    new_link_url = "http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=78b9d599c4f94f8fa3afb1a5458928d6" + "&q=" + keyword
    news_api_request = requests.get(new_link_url)
    api = json.loads(news_api_request.content)

    return render(request, 'entertainmentsearchresults.html', {'api': api})


# Function for constructing TopinUS search results tab
def searchTopUS(request):
    import requests
    import json

    # Store input from input box to variable
    keyword = request.POST.get('mytextbox')

    # Append the keyword to the URL and load search results page with this parameter
    new_link_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=78b9d599c4f94f8fa3afb1a5458928d6" + "&q=" + keyword
    news_api_request = requests.get(new_link_url)
    api = json.loads(news_api_request.content)

    return render(request, 'USsearchresults.html', {'api': api})
