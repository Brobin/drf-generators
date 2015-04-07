
==============
DRF Generators
==============

Writing APIs can be boring and repetitive work. Don't write another CRUDdy view in Django Rest Framework. With DRF Generators, one simple command will create all of your API Views, Serializers, and even Urls for your Django Rest Framework application!

This is not intended to give you a production quality API. It was intended to jumpstart your development and save you from writing the same code over and over for each model.

---------------

|python| |pypi|

---------------

* `Installation`_
* `Usage`_
* `Serializers`_
* `Views`_
* `Urls`_

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

Then run one of the following commands, where ``app`` is the application to generate an API for.

======================== ===================================================
Command                  Action
======================== ===================================================
``generate-serializers`` Generate Serializers for your app.
``generate-views``       Generate Views for your app.
``generate-urls``        Generate urls for your app.
``generate-api``         Generate Serializers, Views, and urls for your app.
======================== ===================================================

.. code-block:: bash

   $ python manage.py {command} {app}

*Note*: In order to use the APIListView classes, you must have the following rest framework DEFAULT_PAGINATION_CLASS and PAGE_SIZE set.

.. code-block:: python

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 15
    }

-----------
Serializers
-----------

The generator will create ``serializers.py`` for your application. DRF Generator currently supports basic serializers with the fields defined in ``models.py``. In the future, foreign key fields for nested serialization will be supported.

.. code-block:: python

    class UserSerializer(ModelSerializer):

        class Meta:
            model = User
            fields = ('id', 'name', 'city', 'state', 'address', 'zip_code')


---------
Views
---------

DRF Generator also takes care of all of your basic CRUD API views using your models and the generated serializers.

DRF Generator creates a basic CRUD API View and List View for each model. The basic CRUD view has methods for ``GET``, ``PUT``, and ``DELETE``. The List View has a ``GET`` method that returns a paginated result of the model, and a ``POST`` method to save a new model.

.. code-block:: python

    class UserAPIView(APIView):

        def get(self, request, id, format=None):
            ...

        def put(self, request, id, format=None):
            ...

        def delete(self, request, id, format=None):
            ...


    class UserAPIListView(APIView):

        def get(self, request, format=None):
            ...

        def post(self, request, format=None):
            ...


----
Urls
----

Finally, DRF Generator will create you a default ``urls.py`` in the following format.

.. code-block:: python

    url(r'^user/([0-9]+)$', views.UserAPIView.as_view()),
    url(r'^user', views.UserAPIListView.as_view()),


.. |python| image:: https://pypip.in/py_versions/drf-generators/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/drf-generators/
    :alt: Supported Python versions

.. |pypi| image:: https://pypip.in/version/drf-generators/badge.svg?text=version&style=flat
    :target: https://pypi.python.org/pypi/drf-generators/
    :alt: Latest Version