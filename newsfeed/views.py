from django.shortcuts import render, redirect
from .models import News, Category
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views import generic
import requests


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


class PostDetail(generic.DetailView):
    model = News
    template_name = 'newsfeed/post_details.html'


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credential')
            return redirect('loign')
    else:
        return render(request, 'newsfeed/login.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('signup')
    else:
        return render(request, 'newsfeed/signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
