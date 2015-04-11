
from django.core.management.base import AppCommand
from drf_generators.generators import *
import django


class Command(AppCommand):
    help = 'Generates DRF API Views and Serializers for a Django app'

    args = "[appname ...]"

    def add_arguments(self, parser):
        parser.add_argument('-f', '--format',
                            dest='format',
                            default='viewset',
                            help='view format (default: viewset)')
        parser.add_argument('--force',
                            dest='force',
                            action='store_true',
                            help='force overwrite files')
        parser.add_argument('--serializers',
                            dest='serializers',
                            action='store_true',
                            help='generate serializers only')
        parser.add_argument('--views',
                            dest='views',
                            action='store_true',
                            help='generate views only')
        parser.add_argument('--urls',
                            dest='urls',
                            action='store_true',
                            help='generate urls only')

    def handle_app_config(self, app_config, **options):
        if app_config.models_module is None:
            raise CommandError('You must provide an app to generate an API')

        force = 'force' in options or False

        if django.VERSION[1] == 7:
            force = 'force' in options or False
            format = 'format' in options or None
            serializers = 'serializers' in options or False
            views = 'views' in options or False
            urls = 'urls' in options or False
        elif django.VERSION[1] == 8:
            force = options['force']
            format = options['format']
            serializers = options['serializers']
            views = options['views']
            urls = options['urls']
        else:
            raise CommandError('You must be using Django 1.7 or 1.8')

        if format == 'viewset':
            generator = ViewSetGenerator(app_config, force)
        elif format == 'apiview':
            generator = APIViewGenerator(app_config, force)
        elif format == 'function':
            generator = FunctionViewGenerator(app_config, force)
        elif format == 'modelviewset' or format is None:
            generator = ModelViewSetGenerator(app_config, force)
        else:
            message = '\'%s\' is not a valid format.' % options['format']
            message += '(viewset, apiview, function)'
            raise CommandError(message)

        if serializers:
            result = generator.generate_serializers()
        elif views:
            result = generator.generate_views()
        elif urls:
            result = generator.generate_urls()
        else:
            result = generator.generate_serializers() + '\n'
            result += generator.generate_views() + '\n'
            result += generator.generate_urls()

        print(result)
