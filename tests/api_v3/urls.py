
from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from api_v3 import views


urlpatterns = [

    url(r'^post/(?P<pk>[0-9]+)$', views.post_detail),
    url(r'^post/$', views.post_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
