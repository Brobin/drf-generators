
from django.core.management.base import AppCommand
from django.db.models import get_models

from drf_generators.generators import *


class Command(AppCommand):
    help = 'Generates DRF API Views and Serializers for a Django app'

    args = "[appname ...]"

    def handle_app_config(self, app_config, **options):
        if app_config.models_module is None:
            raise CommandError('You must provide an app to generate an API')

        generate_serializers(app_config)
        generate_views(app_config)
        generate_urls(app_config)
