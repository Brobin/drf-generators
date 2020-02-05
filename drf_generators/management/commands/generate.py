import sys

from django.core.management.base import AppCommand, CommandError
from drf_generators.generators import *
import django


class Command(AppCommand):
    help = 'Generates DRF API Views and Serializers for a Django app'

    args = "[appname ...]"

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument('-f', '--format', dest='format',
                            default='viewset',
                            help='view format (default: viewset)'),

        parser.add_argument('-d', '--depth', dest='depth', default=0,
                            help='serialization depth'),

        parser.add_argument('--force', dest='force', action='store_true',
                            help='force overwrite files'),

        parser.add_argument('--serializers', dest='serializers',
                            action='store_true',
                            help='generate serializers only'),

        parser.add_argument('--views', dest='views', action='store_true',
                            help='generate views only'),

        parser.add_argument('--urls', dest='urls', action='store_true',
                            help='generate urls only'),

        parser.add_argument('--verbose', dest='verbose', action='store_true',
                            help='Print out logs of file generation'),

    def handle_app_config(self, app_config, **options):
        if app_config.models_module is None:
            raise CommandError('You must provide an app to generate an API')

        if sys.version_info[0] != 3 or sys.version_info[1] < 5:
            raise CommandError('Python 3.5 or newer is required')

        if django.VERSION[1] >= 11 or django.VERSION[0] in [2, 3]:
            force = options['force']
            fmt = options['format']
            depth = options['depth']
            serializers = options['serializers']
            views = options['views']
            urls = options['urls']
        else:
            raise CommandError('You must be using Django 1.11, 2.2, or 3.0')

        if fmt == 'viewset':
            generator = ViewSetGenerator(app_config, force)
        elif fmt == 'apiview':
            generator = APIViewGenerator(app_config, force)
        elif fmt == 'function':
            generator = FunctionViewGenerator(app_config, force)
        elif fmt == 'modelviewset':
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

        if options['verbose']:
            print(result)
