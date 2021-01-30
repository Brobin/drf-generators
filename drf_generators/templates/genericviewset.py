
__all__ = ['GENERIC_URL', 'GENERIC_VIEW']


GENERIC_URL = """from django.conf.urls import include, url
from {{ app }} import views


urlpatterns = [
{% for model in models %}
  url(r'^{{ model|lower }}/(?P<pk>[0-9]+)/$', views.{{ model }}Detail.as_view()),
  url(r'^{{ model|lower }}/$', views.{{ model }}List.as_view()),
{% endfor %}
]
"""


GENERIC_VIEW = """from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from {{ app }}.serializers import {{ serializers|join:', ' }}
from {{ app }}.models import {{ models|join:', ' }}
{% for model in models %}

class {{ model }}List(generics.ListCreateAPIView):
    
    def get_queryset(self):
        queryset = {{ model }}.objects.all()        
        return queryset

    permission_classes = ( IsAuthenticated,)
    serializer_class = {{ model }}Serializer

class {{ model }}Detail(generics.RetrieveUpdateDestroyAPIView):
    
    def get_queryset(self):
        queryset = {{ model }}.objects.all()        
        return queryset
    serializer_class = {{ model }}Serializer
    permission_classes = ( IsAuthenticated,)

{% endfor %}"""
