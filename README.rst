
==============
DRF Generators
==============

Writing API Views is boring and repetitive work. Don't write another CRUDdy view in Django Rest Framework. With DRF Generators, one simple command will create all of your API Views and Serializers for your Django Rest Framework application!

This is not intended to give you porduction quality Views. You may want to add authentication to your View classes. this was intended to save you lots of time writing the same code again and again for each class.

---------------

|python| |pypi|

---------------


------------
Installation
------------

Install with pip:

.. code-block:: bash

    $ pip install drf-generators

Clone the repo and install manually:

.. code-block:: bash

    $ git clone https://github.com/brobin/drf-generators.git
    $ cd drf-generators
    $ python setup.py install


-----
Usage
-----

To use DRF Generator, add it your INSTALLED_APPS.

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'rest_framework',
        'drf_generators',
        ...
    )

Then run the following command, where `app` is the application to generate Serializers and Views for.

.. code-block:: bash

   $ python manage.py generate-api {app}

*Note*: DRF Generators does not yet support generation of urls. you will have to add them in the following format to your project's `urls.py`

.. code-block:: python

    urlpatterns = patterns('',
        url(r'^model', views.ModelListView.as_view()),
        url(r'^model/([0-9]+)$', views.ModelView.as_view()),
    )

*Note*: In order to use the APIListView classes, you must have the following rest framework settings set.

.. code-block:: python

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 15
    }

-----------
Serializers
-----------

The generator will create `serializers.py` for your application. DRF Generator currently supports basic serializers with the fields defined in `models.py`. In the future, foreign key fields for nested serialization will be supported.


---------
API Views
---------

DRF Generator also takes care of all of your basic CRUD API views using your models and the generated serializers.

DRF Generator creates a basic CRUD API View and List View for each model. The basic CRUD view has methods for `GET`, `PUT`, and `DELETE`. The List View has a `GET` method that returns a paginated result of the model, and a `POST` moethod to save a new model.


.. |python| image:: https://pypip.in/py_versions/drf-generators/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/drf-generators/
    :alt: Supported Python versions

.. |pypi| image:: https://pypip.in/version/drf-generators/badge.svg?text=version&style=flat
    :target: https://pypi.python.org/pypi/drf-generators/
    :alt: Latest Version