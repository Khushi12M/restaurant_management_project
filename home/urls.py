from django.urls import path
from .views import contact_view

urlpatterns=[
    path('contact/', contact_view, name='contact'),
    path('contact/sucess/', lamda request: render(request, 'contact_success'),name='contact_sucess'),
]