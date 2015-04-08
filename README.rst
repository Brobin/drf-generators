
==============
DRF Generators
==============

Writing APIs can be boring and repetitive work. Don't write another CRUDdy view in Django Rest Framework. With DRF Generators, one simple command will create all of your API Views, Serializers, and even Urls for your Django Rest Framework application!

This is **not** intended to give you a production quality API. It was intended to jumpstart your development and save you from writing the same code over and over for each model.

Compatible with Django >= 1.7 and Django Rest Framework 3.1.0

---------------

|python| |pypi|

---------------

* `Installation`_
* `Usage`_
* `Serializers`_
* `Views`_
* `Urls`_
* `License`_

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

To use DRF Generator, add it your INSTALLED_APPS.

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'rest_framework',
        'drf_generators',
        ...
    )

*Note*: In order to use the APIListView classes, you must have the rest framework DEFAULT_PAGINATION_CLASS and PAGE_SIZE set.

.. code-block:: python

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 15
    }


-----
Usage
-----

To use the generator run one of the following commands, where ``app`` is the application to generate an API for.

.. code-block:: bash

   $ python manage.py generate {options} {app}

========================== ===================================================
Option                     Action
========================== ===================================================
``--serializers``          Generate only Serializers for your app.
``--views``                Generate only Views for your app.
``--urls``                 Generate only urls for your app.
``--apiview``              Use APIView classes instead of ViewSet classes.
========================== ===================================================


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

By default, DRF Generator will create ViewSet View lcasses like the following for your models.

.. code-block:: python

    class CategoryViewSet(ViewSet):

        def list(self, request):
            ...
        def create(self, request):
            ...
        def retrieve(self, request, pk=None):
            ...
        def update(self, request, pk=None):
            ...
        def destroy(self, request, pk=None):
            ...

When running the generator with the ``--apiview`` option, you will get the following API Views.

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

By default, DRF Generator will create rouserce route based urls like the following.

.. code-block:: python

    router = SimpleRouter()

    router.register(r'model', views.ModelViewSet, 'Model')

    urlpatterns = router.urls

If you run the generatro with the ``--apiview`` option, you will get urls like the following.

.. code-block:: python

    url(r'^user/([0-9]+)$', views.UserAPIView.as_view()),
    url(r'^user', views.UserAPIListView.as_view()),


-------
License
-------

MIT License. See `LICENSE <https://github.com/brobin/drf-generators/blob/master/LICENSE>`_.


.. |python| image:: https://pypip.in/py_versions/drf-generators/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/drf-generators/
    :alt: Supported Python versions

.. |pypi| image:: https://pypip.in/version/drf-generators/badge.svg?text=version&style=flat
    :target: https://pypi.python.org/pypi/drf-generators/
    :alt: Latest Version
