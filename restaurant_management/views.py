from django.conf import settings
from django.shortcuts import render
 def home(request):
    context ={
       'restuarant_name': getattr(setting, 'RESTAURANT_NAME', 'My Restaurant')
       

       }

       return render(request,'home.html', context)
       
        

    