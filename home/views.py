from django.shortcuts import render
from .models import OpeningHour

def home(request):

    hours = OpeningHour.objects.all()
    return render(request."home/home.html",{"hours": hours})