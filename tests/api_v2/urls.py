
from django.conf.urls import patterns, include, url
from django.contrib import admin
from api_v2 import views


urlpatterns = patterns('',

    url(r'^post/(?P<id>[0-9]+)$', views.PostAPIView.as_view()),
    url(r'^post/$', views.PostAPIListView.as_view()),

)
