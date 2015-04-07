import os

__all__ = ['write_file', 'get_model_names', 'get_model_details',
           'get_serializer_names', 'get_view_names']


def write_file(content, filename, app):
    name = os.path.join(os.path.dirname(app.__file__), filename)
    if os.path.exists(name):
        message = 'Are you sure you want to overwrite %s? (y/n)' % filename
        response = input(message)
        if response != 'y':
            return False
    new_file = open(name, 'w+')
    new_file.write(content)
    new_file.close()
    return True


def get_model_names(app_config):
    return [m.__name__ for m in app_config.get_models()]


def get_model_details(app_config):
    details = []
    for m in app_config.get_models():
        m_fields = m._meta.local_fields
        fields = ', '.join(['\'%s\'' % x.name for x in m_fields])
        detail = {'name': m._meta.object_name, 'fields': fields}
        details.append(detail)
    return details


def get_serializer_names(models):
    return [m + 'Serializer' for m in models]


def get_view_names(models):
    api = [m + 'APIView' for m in models]
    api_list = [m + 'APIListView' for m in models]
    return api + api_list
