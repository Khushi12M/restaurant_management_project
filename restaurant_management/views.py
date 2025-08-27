from django.shortcuts import render
from .models import RestaurantInfo

def contact_us(request):
    restaurant= RestaurantInfo.objects.first()
    return render(request.'contact.html',{'restaurant': restaurant})


   


   
       
        

    