
from django.core.management.base import AppCommand
from drf_generators.generators import *


class Command(AppCommand):
    help = 'Generates DRF API Views and Serializers for a Django app'

    args = "[appname ...]"

    def add_arguments(self, parser):
        parser.add_argument('--api-view',
            dest='api-view',
            action='store_true',
            help='Use APIView classes instead of ViewSet classes')

    def handle_app_config(self, app_config, **options):
        if app_config.models_module is None:
            raise CommandError('You must provide an app to generate an API')

        api_view = options['api-view'] or False

        if api_view:
            generator = APIViewGenerator(app_config)
        else:
            generator = ViewSetGenerator(app_config)

        result = generator.generate_serializers()
        print(result)
        result = generator.generate_views()
        print(result)
        result = generator.generate_urls()
        print(result)
