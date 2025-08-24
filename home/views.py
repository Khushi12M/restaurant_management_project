from django.shortcuts import render
def about(request):
    context ={
        "restaurant_name": "My Restaurant",
        "history": "our restaurant was founded in 2005 "
        "mission": "To serve delicious  food with love"
    }

    return render(request,"home/about.html", contaxt)


