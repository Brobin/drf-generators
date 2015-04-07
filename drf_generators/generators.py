
from django import template
import os.path

from drf_generators.templates import *
from drf_generators.helpers import *

__all__ = ['generate_serializers', 'generate_views', 'generate_urls']


def generate_serializers(app_config):
    name = app_config.name
    filename = 'serializers.py'
    message = 'Generating Serializers for %s (%s)' % (name, filename)
    print(message)

    temp = template.Template(SERIALIZER_TEMPLATE)
    models = get_model_names(app_config)
    details = get_model_details(app_config)
    context = template.Context({ 'app': name,
                                 'models': models,
                                 'details': details})

    filename = 'serializers.py'
    content = temp.render(context)
    app = app_config.models_module
    if write_file(content, filename, app):
        print('  - writing %s' % filename)
    else:
        print('Serializer generation cancelled')


def generate_views(app_config):
    app = app_config.models_module
    name = name = app_config.name
    filename = 'views.py'
    message = 'Generating API Views for %s (%s)' % (name, filename)
    print(message)

    temp = template.Template(VIEW_SET_TEMPLATE)
    models = get_model_names(app_config)
    serializers = get_serializer_names(models)
    context = template.Context({ 'app': name,
                                 'serializers': serializers,
                                 'models': models })

    content = temp.render(context)
    if write_file(content, filename, app):
        print('  - writing %s' % filename)
    else:
        print('View genereration cancelled')


def generate_urls(app_config):
    app = app_config.models_module
    name = name = app_config.name
    filename = 'urls.py'
    message = 'Generating urls for %s (%s)' % (name, filename)
    print(message)

    temp = template.Template(VIEW_SET_ROUTER_TEMPLATE)
    models = get_model_names(app_config)
    context = template.Context({ 'app': name,
                                 'models': models })

    content = temp.render(context)
    if write_file(content, filename, app):
        print('  - writing %s' % filename)
    else:
        print('Urls genereration cancelled')
