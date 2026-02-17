from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('landing', views.landing_view, name="landing"),
    path('Register/', views.Register_view, name="Register"),
    path('privacypolicy', views.privacy_view, name="privacypolicy"),
    path('signup', views.signup_view, name="signup"),
    path('login', views.login_view, name="login"),
    path('profile', views.profile_view, name="profile")
]
