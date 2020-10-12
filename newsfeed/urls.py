from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    # path('login/', Login.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
]
