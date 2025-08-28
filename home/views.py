from django.shortcuts import render
from. models import Chef

def about_chef(request):
    chef= Chef.objects.first()
    return render(request,'about_chef.html',{'chef': chef})