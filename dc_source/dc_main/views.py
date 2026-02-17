from django.shortcuts import render

from django.http import HttpRequest

# Create your views here.
def home_view(request:HttpRequest):
    return render(request, "dc_main/home.html")

def landing_view(request:HttpRequest):
    return render(request, "dc_main/landing_page.html")
def Register_view(request:HttpRequest):
    return render(request, "dc_main/Register.html")
