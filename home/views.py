from django.shortcuts import render
from .models import ContactForm

def contact_view(request):
    if request.method =="POST"
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('thank_you')

    else:
        form = ContactForm()
        return render(request. "contact.html", {"form": form})

        def thank_you(request):
            return render(request,'thank_you.html')