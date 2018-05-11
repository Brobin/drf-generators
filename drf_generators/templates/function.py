
__all__ = ['FUNCTION_URL', 'FUNCTION_VIEW']


FUNCTION_URL = """from rest_framework.urlpatterns import format_suffix_patterns
from {{ app }} import views
if django.VERSION[0] == 2:
    from django.urls import path


    urlpatterns = [{% for model in models %}
        path('{{ model|lower }}/<int:pk>', views.{{ model | lower}}_detail),
        path('{{ model|lower }}/', views.views.{{ model | lower}}_list,{% endfor %}
    {% endfor %}
    ]
else:
    from django.conf.urls import url


    urlpatterns = [
    {% for model in models %}
        url(r'^{{ model|lower }}/(?P<pk>[0-9]+)$', views.{{ model | lower }}_detail),
        url(r'^{{ model|lower }}/$', views.{{ model | lower }}_list),
    {% endfor %}
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
"""


FUNCTION_VIEW = """from rest_framework.decorators import api_view
from rest_framework.response import Response
from {{ app }}.models import {{ models | join:', ' }}
from {{ app }}.serializers import {{ serializers | join:', ' }}
{% for model in models %}

@api_view(['GET', 'POST'])
def {{ model | lower }}_list(request):
    if request.method == 'GET':
        items = {{ model }}.objects.all()
        serializer = {{ model }}Serializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = {{ model }}Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def {{ model | lower }}_detail(request, pk):
    try:
        item = {{ model }}.objects.get(pk=pk)
    except {{ model }}.DoesNotExist:
        return Response(status=400)

    if request.method == 'GET':
        serializer = {{ model }}Serializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = {{ model }}Serializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
{% endfor %}"""
