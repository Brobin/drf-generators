
from django.core.management.base import AppCommand
from drf_generators.generators import *


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

        if 'format' in options:
            if options['format'] == 'viewset':
                generator = ViewSetGenerator(app_config, force)
            elif options['format'] == 'apiview':
                generator = APIViewGenerator(app_config, force)
            elif options['format'] == 'function':
                generator = FunctionViewGenerator(app_config, force)
            elif options['format'] == 'modelviewset':
                generator = ModelViewSetGenerator(app_config, force)
            else:
                message = '\'%s\' is not a valid format.' % options['format']
                message += '(viewset, apiview, function)'
                raise CommandError(message)
        else:
            generator = ModelViewSetGenerator(app_config, force)

        if 'serializers' in options:
            result = generator.generate_serializers()
        elif 'views' in options:
            result = generator.generate_views()
        elif 'urls' in options:
            result = generator.generate_urls()
        else:
            result = generator.generate_serializers() + '\n'
            result += generator.generate_views() + '\n'
            result += generator.generate_urls()

        print(result)
