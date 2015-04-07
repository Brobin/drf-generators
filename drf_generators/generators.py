
from django import template
import os.path

from drf_generators.templates import *

__all__ = ['generate_serializers', 'generate_views']


def generate_serializers(models, app):
    name = app.__name__.replace('.models', '')
    message = 'Generating Serializers for %s (serializers.py)' % name
    print(message)

    temp = template.Template(SERIALIZER_FILE_TEMPLATE)
    model_names = [m._meta.object_name for m in models]
    details = []
    for m in models:
        m_fields = m._meta.fields
        fields = ', '.join(['\'%s\'' % x.name for x in m_fields])
        detail = {'name': m._meta.object_name, 'fields': fields}
        details.append(detail)

    context = template.Context({ 'app': name,
                                 'models': model_names,
                                 'details': details})

    name = os.path.join(os.path.dirname(app.__file__), 'serializers.py')
    serializer_file = open(name, 'w+')
    serializer_file.write(temp.render(context))
    serializer_file.close()

    for model in model_names:
        print('  - %sSerializer' % model)

def generate_views(models, app):
    name = app.__name__.replace('.models', '')
    message = 'Generating API Views for %s (models.py)' % name
    print(message)

    temp = template.Template(VIEW_FILE_TEMPLATE)
    model_names = [m._meta.object_name for m in models]
    serializers = [x + 'Serializer' for x in model_names]
    context = template.Context({ 'app': name,
                                 'serializers': serializers,
                                 'models': model_names })

    name = os.path.join(os.path.dirname(app.__file__), 'views.py')
    view_file = open(name, 'w+')
    view_file.write(temp.render(context))
    view_file.close()

    for model in model_names:
        print('  - %sAPIView' % model)
        print('  - %sAPIListView' % model)