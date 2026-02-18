from django.shortcuts import render

from django.http import HttpRequest

from dc_main.permissions import FIELD_PERMISSIONS

from dc_main.choices import (GRADE_CHOICES,
LOCATION_CHOICES,
MOBILITY_CHOICES,
POSITION_CHOICES,
POTENTIAL_GRADE_CHOICES,
SUCCESSION_PLAN_CHOICES,
ACTION_STATUS_CHOICES,
DEV_CELL_RATING_CHOICES,
PERFORMANCE_RATING_CHOICES)


# Create your views here.
def home_view(request:HttpRequest):
    return render(request, "dc_main/home.html")

def main_form_view(request:HttpRequest):
    request.user.role = "Administrator"
    return render(request, "dc_main/main_form.html", {
    "FIELD_PERMISSIONS" : FIELD_PERMISSIONS,
    "user" : request.user,
    "GRADE_CHOICES" : GRADE_CHOICES,
    "LOCATION_CHOICES" : LOCATION_CHOICES,
    "MOBILITY_CHOICES" : MOBILITY_CHOICES,
    "POSITION_CHOICES" : POSITION_CHOICES,
    "POTENTIAL_GRADE_CHOICES" : POTENTIAL_GRADE_CHOICES,
    "SUCCESSION_PLAN_CHOICES" : SUCCESSION_PLAN_CHOICES,
    "ACTION_STATUS_CHOICES" : ACTION_STATUS_CHOICES,
    "DEV_CELL_RATING_CHOICES" : DEV_CELL_RATING_CHOICES,
    "PERFORMANCE_RATING_CHOICES" : PERFORMANCE_RATING_CHOICES
    })

def configured_list_editor_view(request:HttpRequest):
    request.user.role = "Administrator"

