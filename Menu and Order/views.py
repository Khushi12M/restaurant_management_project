from django.shortcuts import render
from .models import MenuItem

def menu_page(request):
    menu_items= MenuItem.objects.all().order_by('category', 'name')
    