from django.shortcuts import render
from .models import News, Category


def index(request):
    news = None
    categories = Category.get_all_category()
    categoryID = request.GET.get('category')
    if categoryID:
        news = News.get_all_products_by_categoryid(categoryID)
    else:
        news = News.get_all_news()

    data = {}
    data['news'] = news
    data['categories'] = categories

    return render(request, 'newsfeed/index.html', data)
