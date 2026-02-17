from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('login', views.login_view, name="login"),
    path('signup', views.signup_view, name="signup"),
    path('info-packs', views.info_view, name="infopacks"),
]