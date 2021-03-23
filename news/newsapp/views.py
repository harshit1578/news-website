from django.shortcuts import render
def home(request):
    import requests
    import json
    news_api_request=requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=57da676cc82b44ca92e988ef713b600d")
    api=json.loads(news_api_request.content)
    return render(request,'home.html',{'api':api})
