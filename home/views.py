from django.shortcuts import render
from Menu_and_Order.models import MenuItem

def home_view(request):
    query= request.GET.get('q')
    if query:
        menu_items =MenuItem.objects.filter(name_icontains=query)
        else:
            menu_items= MenuItem.objects.all()

            return render(request,'home.html',{'menu_items': menu_items,'query': query})