from django.shortcuts import render
from .models import RestaurantInfo

def homepage(request):
    restaurant= RestaurantInfo.objects.first()
    return render(request, "home/index.html",{"restaurant": reataurant})
