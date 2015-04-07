
from django import template
import os.path

from drf_generators.templates import *
from drf_generators.helpers import write_file

__all__ = ['generate_serializers', 'generate_views']


def generate_serializers(models, app, name):
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

    filename = 'serializers.py'
    content = temp.render(context)
    if write_file(content, filename, app):
        for model in model_names:
            print('  - %sSerializer' % model)
    else:
        print('Serializer generation cancelled')

def generate_views(models, app, name):
    message = 'Generating API Views for %s (models.py)' % name
    print(message)

    temp = template.Template(VIEW_FILE_TEMPLATE)
    model_names = [m._meta.object_name for m in models]
    serializers = [x + 'Serializer' for x in model_names]
    context = template.Context({ 'app': name,
                                 'serializers': serializers,
                                 'models': model_names })

    filename = 'views.py'
    content = temp.render(context)
    if write_file(content, filename, app):
        for model in model_names:
            print('  - %sAPIView' % model)
            print('  - %sAPIListView' % model)
    else:
        print('View genereration cancelled')