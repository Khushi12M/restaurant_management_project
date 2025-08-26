from django.shortcuts import render
from .models import ContactForm

def contact_view(request):
    if request.method =="POST"
    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
{}
        print(f"New messgae from {name} ("{email}): {message}")

 
    return render(request."home/contact_success.html",{"name": name})
    else:
        form = ContactForm()
        return render(request. "home/contact.html", {"form": form})