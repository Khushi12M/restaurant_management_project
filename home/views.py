from django.shortcuts import render
 def home(request):
    breadcrumbs=[
        {"title": "Home", "url": "/"},

    ]
    return render(request,"home.html", {"breadcrumbs": breadcrumbs})


