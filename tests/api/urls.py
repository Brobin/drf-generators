from django.conf.urls import include, url
try:
  from django.conf.urls import patterns
except ImportError:
  pass
import django
from django.contrib import admin
from api import views

if django.VERSION[1] < 10 and django.VERSION[0] == 1:
  urlpatterns = patterns('',
  
    url(r'^category/(?P<id>[0-9]+)$', views.CategoryAPIView.as_view()),
    url(r'^category/$', views.CategoryAPIListView.as_view()),
  
    url(r'^post/(?P<id>[0-9]+)$', views.PostAPIView.as_view()),
    url(r'^post/$', views.PostAPIListView.as_view()),
  
  )
else:
  urlpatterns = [
  
    url(r'^category/(?P<id>[0-9]+)$', views.CategoryAPIView.as_view()),
    url(r'^category/$', views.CategoryAPIListView.as_view()),
  
    url(r'^post/(?P<id>[0-9]+)$', views.PostAPIView.as_view()),
    url(r'^post/$', views.PostAPIListView.as_view()),
  
  ]
