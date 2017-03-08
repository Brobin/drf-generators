import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='drf-generators',
    version='0.3.0',

    description='Generate DRF Serializers, Views, and urls for your API aplication.',
    long_description=README,

    url='https://github.com/brobin/drf-generators',
    download_url = 'https://github.com/brobin/drf-generators/archive/0.3.0.zip',
    author='Tobin Brown',
    author_email='tobin@brobin.me',

    license='MIT',

    packages=['drf_generators', 'drf_generators.templates', 'drf_generators.management', 'drf_generators.management.commands'],
    include_package_data=True,
    install_requires=['Django>=1.7'],

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ],

    keywords='API REST framework generate scaffold',
)
