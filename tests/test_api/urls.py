from django.conf.urls import include, url
from django.contrib import admin

from django import VERSION

if VERSION[0] == 1:
    urlpatterns = [

        url(r'^admin/', include(admin.site.urls)),
        url(r'^api/', include('api.urls')),

    ]

else:

    urlpatterns = [

        url(r'^admin/', admin.site.urls),
        url(r'^api/', include('api.urls')),

    ]