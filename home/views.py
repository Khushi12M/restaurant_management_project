
from. models import Chef
def home(request):

    chef= chef.objects.first()
    return render(request,'home.html', {'chef': chef})
