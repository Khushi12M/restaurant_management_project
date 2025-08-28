from django.core.paginator import Paginator
from django.shortcuts import render
from .models import MenuItem

def menu_view(request):
    menu_items= MenuItem.objects.all()
    paginator= Paginator(menu_items,5)

    page_number= request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'menu.html',{'page_obj': page_obj})
    