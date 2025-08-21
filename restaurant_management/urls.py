from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns[
    path('', include('home.urls')),
    path('menu/', include('Menu and order.urls')),
]

if settings.DEBUG:
    urlpattern+= static(settings.MEDIA_URL,document_root=settins.MEDIA_ROOT)

