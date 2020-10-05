from django.shortcuts import render
from .models import News


# Create your views here.
def index(request):
    news = News.get_all_news()
    return render(request, 'newsfeed/index.html', {'news': news})
