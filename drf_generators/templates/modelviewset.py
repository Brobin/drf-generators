
__all__ = ['MODEL_VIEW_SET_URL', 'MODEL_VIEW_SET_VIEW']


VIEW_SET_URL = """
from rest_framework.routers import SimpleRouter
from {{ app }} import views


router = SimpleRouter()
{% for model in models %}
router.register(r'{{ model | lower }}', views.{{ model }}ViewSet){% endfor %}

urlpatterns = router.urls
"""


VIEW_SET_VIEW = """
from rest_framework.viewsets import ModelViewSet
from {{ app }}.serializers import {{ serializers|join:', ' }}
from {{ app }}.models import {{ models|join:', ' }}
{% for model in models %}

class {{ model }}ViewSet(ModelViewSet):
    queryset = {{ model }}.objects.all()
    serializer_class = {{ model }}Serializer
{% endfor %}
"""
