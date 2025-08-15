
from datetime import datetime
from django.shortcuts import render
  
def home(request):
    return render(request, 'homepage.html', {'year': datetime.now().year})