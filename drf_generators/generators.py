
from django.template import Template, Context
import os.path

from drf_generators.templates import *
from drf_generators.helpers import write_file

__all__ = ['APIViewGenerator', 'ViewSetGenerator']


class BaseGenerator(object):

    def __init__(self, app_config):
        self.app_config = app_config
        self.app = app_config.models_module
        self.name = app_config.name
        self.serializer_template = Template(SERIALIZER)
        self.models = self.get_model_names()

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
        details = self.get_model_details()
        context = Context({ 'app': self.name, 'models': self.models, 
                            'details': details})
        content = self.serializer_template.render(context)
        return content

    def view_content(self):
        context = Context({ 'app': self.name, 'models': self.models,})
        return self.view_template.render(context)

    def url_content(self):
        context = Context({'app': self.name, 'models': self.models})
        return self.url_template.render(context)

    def get_model_details(self):
        details = []
        for m in self.app_config.get_models():
            m_fields = m._meta.local_fields
            fields = ', '.join(['\'%s\'' % x.name for x in m_fields])
            detail = {'name': m._meta.object_name, 'fields': fields}
            details.append(detail)
        return details

    def get_model_names(self):
        return [m.__name__ for m in self.app_config.get_models()]


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

