from django import VERSION


if VERSION[0] == 1:
    from django.conf.urls import include, url
    urlpatterns = [
        url(r'^api/', include('api.urls')),
    ]

else:
    from django.urls import include, path
    urlpatterns = [
        path('api/', include('api.urls')),
    ]
