from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('Register/', views.Register_view, name="Register"),
]