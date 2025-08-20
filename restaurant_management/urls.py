from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpattern=[
    path('', include('home.urls')),
    path('menu/', include('menu and order.urls')),

]

if settings.DEBUG
urlpattern +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
