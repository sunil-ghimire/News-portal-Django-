from django.shortcuts import render, redirect
from .models import News, Category
from django.contrib.auth.models import User, auth
from django.contrib import messages


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


# def validateCustomer(customer):
#     error_message = None
#     if not customer.first_name:
#         error_message = "First Name Required !!"
#     elif len(customer.first_name) < 4:
#         error_message = 'First Name must be 4 char long or more'
#     elif not customer.last_name:
#         error_message = 'Last Name Required'
#     elif len(customer.last_name) < 4:
#         error_message = 'Last Name must be 4 char long or more'
#     elif len(customer.password) < 6:
#         error_message = 'Password must be 6 char long'
#     elif len(customer.password1) < 6 and customer.password != customer.password1:
#         error_message = 'Password do not match!'
#     elif len(customer.email) < 5:
#         error_message = 'Email must be 5 char long'
#     elif customer.isExist():
#         error_message = 'Email Address Already Registered'
#     return error_message
#
#
# def registerUser(request):
#     first_name = request.POST['first_name']
#     last_name = request.POST['last_name']
#     username = request.POST['username']
#     email = request.POST['email']
#     password = request.POST['password']
#     password1 = request.POST['password1']
#
#     values = {
#         'username': username,
#         'first_name': first_name,
#         'last_name': last_name,
#         'email': email
#     }
#     user = User.objects.create_user(username=username,
#                                     password=password,
#                                     first_name=first_name,
#                                     last_name=last_name,
#                                     email=email)
#     error_message = validateCustomer(user)
#     if not error_message:
#         user.save()
#         print("user Created")
#         return redirect('/')
#     else:
#         data = {
#             'error_message': error_message,
#             'values': values
#         }
#         return render(request, 'newsfeed/signup.html', data)
#
#
# def signup(request):
#     if request.method == "GET":
#         return render(request, 'newsfeed/signup.html', {})
#     else:
#         return registerUser(request)
#
#
# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = auth.authenticate(email=email, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')
#         else:
#             messages.info(request, 'invalid credentials')
#             return redirect('login')
#     else:
#         return render(request, 'newsfeed/login.html')
#
#

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
