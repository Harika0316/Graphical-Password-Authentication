from django import views
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('homesignup', views.homesignup, name='homesignup'),
    path('homesignin', views.homesignin, name='homesignin'),
    path('signin', views.signin, name='signin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('forgot', views.forgot, name='forgot'),
    path('homeforgot', views.homeforgot, name='homeforgot'),
]
