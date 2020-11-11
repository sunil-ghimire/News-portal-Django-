from django.urls import path, include
from . import views
from .views import NewsView

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('article/<int:id>', views.post_details, name='post_details'),

    # api path
    path('api/', NewsView.as_view()),
]
