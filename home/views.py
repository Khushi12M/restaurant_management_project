from django.shortcuts import render
from  restaurant_management .models import RestaurantInfo

def contact_view(request):
    restaurant = RestaurantInfo.objects.first()
    return render(request,'contact.html',{'restaurant: restaurant'})
   