
__all__ = ['API_VIEW', 'API_URL']


API_URL = """from django.conf.urls import include, url
from {{ app }} import views


urlpatterns = [
{% for model in models %}
  url(r'^{{ model|lower }}/(?P<id>[0-9]+)/$', views.{{ model }}APIView.as_view()),
  url(r'^{{ model|lower }}/$', views.{{ model }}APIListView.as_view()),
{% endfor %}
]
"""


API_VIEW = """from rest_framework.pagination import PageNumberPagination
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
        items = {{ model }}.objects.order_by('pk')
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
{% endfor %}"""
