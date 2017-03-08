__all__ = ['SERIALIZER']


SERIALIZER = """from rest_framework.serializers import ModelSerializer
from {{ app }}.models import {{ models | join:', ' }}
{% for model in models %}

class {{ model }}Serializer(ModelSerializer):

    class Meta:
        model = {{ model }}{% if depth != 0 %}
        depth = {{ depth }}{% endif %}
        fields = '__all__'
{% endfor %}"""
