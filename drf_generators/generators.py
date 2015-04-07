
from django import template
import os.path

from drf_generators.templates import *
from drf_generators.helpers import write_file

__all__ = ['generate_serializers', 'generate_views', 'generate_urls']


def generate_serializers(app_config):
    app = app_config.models_module
    name = name = app_config.name
    filename = 'serializers.py'
    message = 'Generating Serializers for %s (%s)' % (name, filename)
    print(message)

    temp = template.Template(SERIALIZER_FILE_TEMPLATE)
    model_names = [m.__name__ for m in app_config.get_models()]
    details = []
    for m in app_config.get_models():
        m_fields = m._meta.local_fields
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


def generate_views(app_config):
    app = app_config.models_module
    name = name = app_config.name
    filename = 'views.py'
    message = 'Generating API Views for %s (%s)' % (name, filename)
    print(message)

    temp = template.Template(VIEW_FILE_TEMPLATE)
    model_names = [m.__name__ for m in app_config.get_models()]
    serializers = [x + 'Serializer' for x in model_names]
    context = template.Context({ 'app': name,
                                 'serializers': serializers,
                                 'models': model_names })

    content = temp.render(context)
    if write_file(content, filename, app):
        for model in model_names:
            print('  - %sAPIView' % model)
            print('  - %sAPIListView' % model)
    else:
        print('View genereration cancelled')


def generate_urls(app_config):
    app = app_config.models_module
    name = name = app_config.name
    filename = 'urls.py'
    message = 'Generating urls for %s (%s)' % (name, filename)
    print(message)

    temp = template.Template(URL_FILE_TEMPLATE)
    model_names = [m.__name__ for m in app_config.get_models()]
    context = template.Context({ 'app': name,
                                 'models': model_names })

    content = temp.render(context)
    if write_file(content, filename, app):
        print('  - writing %s' % filename)
    else:
        print('Urls genereration cancelled')
