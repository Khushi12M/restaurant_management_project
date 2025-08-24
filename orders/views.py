from django.shortcuts import render
import random

def order_confirmation(request):
    order_number= random.randint(1000,9999)

    return render(request, 'order_confirmation.html',{'order_number': order_number})
 
# Create your views here.
