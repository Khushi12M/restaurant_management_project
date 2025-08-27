from django.shortcuts import render
from .import views

urlpatterns[
    path('contact/',views.contact_view. name='contact'),
    path('thank_you', views.thank_you_view, name='thank_you'),
]


    
]