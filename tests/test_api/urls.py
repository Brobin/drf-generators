from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('api_v1.urls')),
    url(r'^api/v2/', include('api_v2.urls')),

]
