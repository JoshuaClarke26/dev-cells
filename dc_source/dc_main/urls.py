from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('form/', views.main_form_view, name="main form"),
    path('config/', views.configured_list_editor_view, name="cfev"),
]