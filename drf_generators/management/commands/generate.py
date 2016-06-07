
from django.core.management.base import AppCommand, CommandError
from django.utils.module_loading import import_module
from drf_generators.generators import *
from drf_generators import generators as generators_module
from optparse import make_option
import django

# dict of submodule name => [imported symbols]
template_imports = {
    'serializer': ['SERIALIZER'],
    'apiview': ['API_URL', 'API_VIEW'],
    'viewset': ['VIEW_SET_URL', 'VIEW_SET_VIEW'],
    'function': ['FUNCTION_URL', 'FUNCTION_VIEW'],
    'modelviewset': ['MODEL_URL', 'MODEL_VIEW'],
}


class Command(AppCommand):
    help = 'Generates DRF API Views and Serializers for a Django app'

    args = "[appname ...]"

    base_options = (
        make_option('-f', '--format', dest='format', default='viewset',
                    help='view format (default: viewset)'),

        make_option('-d', '--depth', dest='depth', default=0,
                    help='serialization depth'),

        make_option('--force', dest='force', action='store_true',
                    help='force overwrite files'),

        make_option('--serializers', dest='serializers', action='store_true',
                    help='generate serializers only'),

        make_option('--views', dest='views', action='store_true',
                    help='generate views only'),

        make_option('--urls', dest='urls', action='store_true',
                    help='generate urls only'),

        make_option('-t', '--template', dest='template',
                    help='package name to use for templates')
    )

    option_list = AppCommand.option_list + base_options

    def handle_app_config(self, app_config, **options):
        if app_config.models_module is None:
            raise CommandError('You must provide an app to generate an API')

        if django.VERSION[1] == 7:
            force = options['force'] if 'force' in options else False
            format = options['format'] if 'format' in options else None
            depth = options['depth'] if 'depth' in format else 0
            if 'serializers' in options:
                serializers = options['serializers']
            else:
                serializers = False
            views = options['views'] if 'views' in options else False
            urls = options['urls'] if 'urls' in options else False
            template = options['template'] if 'template' in options else None

        elif django.VERSION[1] >= 8:
            force = options['force']
            format = options['format']
            depth = options['depth']
            serializers = options['serializers']
            views = options['views']
            urls = options['urls']
            template = options['template']
        else:
            raise CommandError('You must be using Django 1.7, 1.8 or 1.9')

        if template is not None:
            for submodule, symbols in template_imports.items():
                mod = import_module('%s.%s' % (template, submodule))
                for s in symbols:
                    setattr(generators_module, s, getattr(mod, s))

        if format == 'viewset':
            generator = ViewSetGenerator(app_config, force)
        elif format == 'apiview':
            generator = APIViewGenerator(app_config, force)
        elif format == 'function':
            generator = FunctionViewGenerator(app_config, force)
        elif format == 'modelviewset':
            generator = ModelViewSetGenerator(app_config, force)
        else:
            message = '\'%s\' is not a valid format. ' % options['format']
            message += '(viewset, modelviewset, apiview, function)'
            raise CommandError(message)

        if serializers:
            result = generator.generate_serializers(depth)
        elif views:
            result = generator.generate_views()
        elif urls:
            result = generator.generate_urls()
        else:
            result = generator.generate_serializers(depth) + '\n'
            result += generator.generate_views() + '\n'
            result += generator.generate_urls()

        print(result)
