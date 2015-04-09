
from django.template import Template, Context
import os.path

from drf_generators.templates.serializer import SERIALIZER
from drf_generators.templates.apiview import API_URL, API_VIEW
from drf_generators.templates.viewset import VIEW_SET_URL, VIEW_SET_VIEW
from drf_generators.templates.function import FUNCTION_URL, FUNCTION_VIEW
from drf_generators.helpers import write_file

__all__ = ['BaseGenerator', 'APIViewGenerator', 'ViewSetGenerator',
           'FunctionViewGenerator']


class BaseGenerator(object):

    def __init__(self, app_config):
        self.app_config = app_config
        self.app = app_config.models_module
        self.name = app_config.name
        self.serializer_template = Template(SERIALIZER)
        self.models = self.get_model_names()
        self.serializers = self.get_serializer_names()

    def generate_serializers(self):
        content = self.serializer_content()
        filename = 'serializers.py'
        if write_file(content, filename, self.app):
            return '  - writing %s' % filename
        else:
            return 'Serializer generation cancelled'

    def generate_views(self):
        content = self.view_content()
        filename = 'views.py'
        if write_file(content, filename, self.app):
            return '  - writing %s' % filename
        else:
            return 'View generation cancelled'

    def generate_urls(self):
        content = self.url_content()
        filename = 'urls.py'
        if write_file(content, filename, self.app):
            return '  - writing %s' % filename
        else:
            return 'Url generation cancelled'

    def serializer_content(self):
        context = Context({'app': self.name, 'models': self.models})
        return self.serializer_template.render(context)

    def view_content(self):
        context = Context({'app': self.name, 'models': self.models,
                           'serializers': self.serializers})
        return self.view_template.render(context)

    def url_content(self):
        context = Context({'app': self.name, 'models': self.models})
        return self.url_template.render(context)

    def get_model_names(self):
        return [m.__name__ for m in self.app_config.get_models()]

    def get_serializer_names(self):
        return [m + 'Serializer' for m in self.models]


class APIViewGenerator(BaseGenerator):

    def __init__(self, app_config):
        self.view_template = Template(API_VIEW)
        self.url_template = Template(API_URL)
        super(APIViewGenerator, self).__init__(app_config)


class ViewSetGenerator(BaseGenerator):

    def __init__(self, app_config):
        self.view_template = Template(VIEW_SET_VIEW)
        self.url_template = Template(VIEW_SET_URL)
        super(ViewSetGenerator, self).__init__(app_config)

class FunctionViewGenerator(BaseGenerator):

    def __init__(self, app_config):
        self.view_template = Template(FUNCTION_VIEW)
        self.url_template = Template(FUNCTION_URL)
        super(FunctionViewGenerator, self).__init__(app_config)

