from django.shortcuts import render
from .models import News, Category, Customer
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password, check_password


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


def validateCustomer(customer):
    error_message = None
    if not customer.first_name:
        error_message = "First Name Required !!"
    elif len(customer.first_name) < 4:
        error_message = 'First Name must be 4 char long or more'
    elif not customer.last_name:
        error_message = 'Last Name Required'
    elif len(customer.last_name) < 4:
        error_message = 'Last Name must be 4 char long or more'
    elif not customer.phone:
        error_message = 'Phone Number required'
    elif len(customer.phone) < 10:
        error_message = 'Phone Number must be 10 char Long'
    elif len(customer.password) < 6:
        error_message = 'Password must be 6 char long'
    elif len(customer.email) < 5:
        error_message = 'Email must be 5 char long'
    elif customer.isExist():
        error_message = 'Email Address Already Registered'
    return error_message


def registerUser(request):
    postData = request.POST
    first_name = postData.get('fname')
    last_name = postData.get('lname')
    phone = postData.get('phone')
    email = postData.get('email')
    password = postData.get('password')

    values = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'email': email
    }

    customer = Customer(first_name=first_name,
                        last_name=last_name,
                        phone=phone,
                        email=email,
                        password=password)
    error_message = validateCustomer(customer)

    if not error_message:
        customer.password = make_password(customer.password)
        customer.register()
        return redirect('index')
    else:
        data = {
            'error_message': error_message,
            'values': values
        }
        return render(request, 'newsfeed/signup.html', data)


def signup(request):
    if request.method == "GET":
        return render(request, 'newsfeed/signup.html', {})
    else:
        return registerUser(request)


def login(request):
    if request.method == "GET":
        return render(request, 'newsfeed/login.html', {})
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Customer and get_customer_by_email(email) is from models.py file
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect('index')
            else:
                error_message = "Email or Password Invalid"
        else:
            error_message = "Email or Password Invalid"
        print(email, password)
        print(customer)
        return render(request, 'newsfeed/login.html', {'error_message': error_message})
