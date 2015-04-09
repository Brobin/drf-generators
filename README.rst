
==============
DRF Generators
==============

Writing APIs can be boring and repetitive work. Don't write another CRUDdy view in Django Rest Framework. With DRF Generators, one simple command will create all of your API Views, Serializers, and even Urls for your Django Rest Framework application!

This is **not** intended to give you a production quality API. It was intended to jumpstart your development and save you from writing the same code over and over for each model.

Compatible with Django >= 1.7 and Django Rest Framework 3.1.0

---------------

|python| |pypi| |license|

---------------

* `Installation`_
* `Usage`_
* `Serializers`_
* `Views`_
* `Urls`_
* `Tests`_
* `License`_

---------------

============
Installation
============

Install with pip:

.. code-block:: bash

    $ pip install drf-generators

or Clone the repo and install manually:

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

*Note*: In order to use the APIView classes, you must have the rest framework DEFAULT_PAGINATION_CLASS and PAGE_SIZE set.

.. code-block:: python

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 15
    }

-----------------

=====
Usage
=====

To use the generator the following command, where ``app`` is the application to generate an API for.

.. code-block:: bash

   $ python manage.py generate {app} {options}

========================== ===================================================
Option                     Action
========================== ===================================================
``--serializers``          Generate only Serializers for your app.
``--views``                Generate only Views for your app.
``--urls``                 Generate only urls for your app.
``-f``, ``--format``       Format to use when generating views and urls. Valid options: viewset, apiview, function. Default: viewset.
========================== ===================================================

-------------------

===========
Serializers
===========

Drf Generators will create ``serializers.py`` for your application. IT currently uses rest framework's ``ModelSerializer`` for base serialization of the models defined in ``models.py``.

.. code-block:: python

    class ModelSerializer(serializers.ModelSerializer):

        class Meta:
            model = User

------------------

=====
Views
=====

DRF Generators will create ``views.py`` for your application. It can generate ``ViewSet``, ``APIView`` and function based views. Set the ``--format`` option when running the generator to pick the preferred style

-------
ViewSet
-------

``--format viewset``

.. code-block:: python

    class ModelViewSet(ViewSet):

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

-------
APIView
-------

``--format apiview``

.. code-block:: python

    class ModelAPIView(APIView):

        def get(self, request, id, format=None):
            ...
        def put(self, request, id, format=None):
            ...
        def delete(self, request, id, format=None):
            ...

    class ModelAPIListView(APIView):

        def get(self, request, format=None):
            ...
        def post(self, request, format=None):
            ...

--------
Function
--------

``--format function``

.. code-block:: python

    @api_view(['GET', 'POST'])
    def model_list(request):
        if request.method == 'GET':
            ...
        elif request.method == 'POST':
            ...

    @api_view(['GET', 'PUT', 'DELETE'])
    def model_detail(request, pk):
        if request.method == 'GET':
            ...
        elif request.method == 'PUT':
            ...
        elif request.method == 'DELETE':
            ...

-----------------

====
Urls
====

Finally, DRF Generator will create you a default ``urls.py`` to match the View format you are using.

--------------
ViewSet Routes
--------------

.. code-block:: python

    router = SimpleRouter()

    router.register(r'model', views.ModelViewSet, 'Model')

    urlpatterns = router.urls

------------
APIView urls
------------

.. code-block:: python

    url(r'^model/([0-9]+)$', views.ModelAPIView.as_view()),
    url(r'^model', views.ModelAPIListView.as_view()),

-------------
Function urls
-------------

.. code-block:: python

    urlpatterns = [

        url(r'^model/(?P<pk>[0-9]+)$', views.model_detail),
        url(r'^model/$', views.model_list),

    ]

    urlpatterns = format_suffix_patterns(urlpatterns)


=====
Tests
=====

A full application built with drf-generators can be found in the `tests directory <http://github.com/brobin/drf-generators/tree/master/tests>`_. Instructions on running them can be found in the test project's README.


=======
License
=======

MIT License. See `LICENSE <https://github.com/brobin/drf-generators/blob/master/LICENSE>`_.


.. |python| image:: https://pypip.in/py_versions/drf-generators/badge.svg?style=flat-square
    :target: https://pypi.python.org/pypi/drf-generators/
    :alt: Supported Python versions

.. |pypi| image:: https://pypip.in/version/drf-generators/badge.svg?text=version&style=flat-square
    :target: https://pypi.python.org/pypi/drf-generators/
    :alt: Latest Version

.. |license| image:: https://pypip.in/license/drf-generators/badge.svg?style=flat-square
    :target: https://pypi.python.org/pypi/drf-generators/
    :alt: License
