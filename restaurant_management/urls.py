from django.conf import admin
from django.urls import path, include
from home import views

urlpatterns[
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
  
]

