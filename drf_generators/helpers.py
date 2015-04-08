import os

__all__ = ['write_file']


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
