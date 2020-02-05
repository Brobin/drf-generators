
__all__ = ['VIEW_SET_URL', 'VIEW_SET_VIEW']


VIEW_SET_URL = """from rest_framework.routers import SimpleRouter
from {{ app }} import views


router = SimpleRouter()
{% for model in models %}
router.register(r'{{ model | lower }}', views.{{ model }}ViewSet, '{{model}}'){% endfor %}

urlpatterns = router.urls
"""


VIEW_SET_VIEW = """from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from {{ app }}.serializers import {{ serializers|join:', ' }}
from {{ app }}.models import {{ models|join:', ' }}
{% for model in models %}

class {{ model }}ViewSet(ViewSet):

    def list(self, request):
        queryset = {{ model }}.objects.order_by('pk')
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
{% endfor %}"""
