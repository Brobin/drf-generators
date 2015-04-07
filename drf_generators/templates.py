"""
Templates for generatring DRF Serializer and View classes.
"""

__all__ = ['SERIALIZER_TEMPLATE', 'API_VIEW_TEMPLATE',
           'API_URL_TEMPLATE', 'VIEW_SET_ROUTER_TEMPLATE',
           'VIEW_SET_TEMPLATE']


SERIALIZER_TEMPLATE = """
from rest_framework.serializers import ModelSerializer
from {{ app }}.models import {{ models | join:', ' }}

{% for detail in details %}
class {{ detail.name }}Serializer(ModelSerializer):

    class Meta:
        model = {{ detail.name }}
        fields = ({{ detail.fields | safe }})

{% endfor %}"""


API_URL_TEMPLATE = """
from django.conf.urls import patterns, include, url
from django.contrib import admin
from {{ app }} import views


urlpatterns = patterns('',
{% for model in models %}
    url(r'^{{ model|lower }}/([0-9]+)$', views.{{ model }}APIView.as_view()),
    url(r'^{{ model|lower }}', views.{{ model }}APIListView.as_view()),
{% endfor %}
)
"""


API_VIEW_TEMPLATE = """
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from {{ app }}.serializers import {{ serializers|join:', ' }}
from {{ app }}.models import {{ models|join:', ' }}
{% for model in models %}

class {{ model }}APIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = {{ model }}.objects.get(pk=id)
            serializer = {{ model }}Serializer(item)
            return Response(serializer.data)
        except {{ model }}.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = {{ model }}.objects.get(pk=id)
        except {{ model }}.DoesNotExist:
            return Response(status=404)
        serializer = {{ model }}Serializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = {{ model }}.objects.get(pk=id)
        except {{ model }}.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class {{ model }}APIListView(APIView):

    def get(self, request, format=None):
        items = {{ model }}.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = {{ model }}Serializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = {{ model }}Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
{% endfor %}
"""


VIEW_SET_ROUTER_TEMPLATE = """
from rest_framework.routers import DefaultRouter
from {{ app }} import views


router = DefaultRouter()
{% for model in models %}
router.register(r'{{ model | lower }}', views.{{ model }}ViewSet){% endfor %}

urlpatterns = router.urls
"""


VIEW_SET_TEMPLATE = """
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from {{ app }}.serializers import {{ serializers|join:', ' }}
from {{ app }}.models import {{ models|join:', ' }}
{% for model in models %}

class {{ model }}ViewSet(ViewSet):

    def list(self, request):
        queryset = {{ model }}.objects.all()
        serializer = {{ model }}Serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = {{ model }}Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = {{ model }}.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = {{ model }}Serializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = {{ model }}.objects.get(pk=pk)
        except {{ model }}.DoesNotExist:
            return Response(status=404)
        serializer = {{ model }}Serializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = {{ model }}.objects.get(pk=pk)
        except {{ model }}.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
{% endfor %}
"""
