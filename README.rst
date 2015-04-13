==============
DRF Generators
==============

Writing APIs can be boring and repetitive work. Don't write another CRUDdy view in `Django Rest Framework <http://github.com/tomchristie/django-rest-framework>`_. With DRF Generators, one simple command will generate all of your Views, Serializers, and even Urls for your Django Rest Framework application!

For a full step-by-step tutorial, check out my `blog post <http://brobin.me/blog/2015/4/13/how-to-quickly-write-an-api-in-django>`_!

This is **not** intended to give you a production quality API. It was intended to jumpstart your development and save you from writing the same code over and over for each model.

---------------

|python| |pypi| |license| |travis| |django| |drf|

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

To use DRF Generators, add it your INSTALLED_APPS.

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

To use the generators, run the following command, where ``app`` is the application to generate an API for.

.. code-block:: bash

   $ python manage.py generate {app} {options}

========================== ===================================================
Option                     Action
========================== ===================================================
``--serializers``          Generate only Serializers for your app.
``--views``                Generate only Views for your app.
``--urls``                 Generate only urls for your app.
``--force``                Overwrite existing files without the warning prompt.
``-f``, ``--format``       Format to use when generating views and urls. Valid options: ``viewset``, ``apiview``, ``function``, ``modelviewset``. Default: ``viewset``.
========================== ===================================================

**Example:** Generate everything for the app ``api_v1`` with function style views, overwriting existing files.

.. code-block:: bash

    $ python manage.py generate api_v1 --format function --force

-------------------

===========
Serializers
===========

Drf Generators will create ``serializers.py`` for your application. It currently uses rest framework's ``ModelSerializer`` for serialization of the models defined in ``models.py``.

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

``python manage.py generate api  --format viewset``

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

``python manage.py generate api --format apiview``

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

``python manage.py generate api --format function``

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

-------------
ModelViewSet
-------------

``python manage.py generate api --format modelviewset``

.. code-block:: python

    class MyModelViewSet(ModelViewSet):
        queryset = MyModel.objects.all()
        serializer_class = MyModelSerializer

-----------------

====
Urls
====

Finally, DRF Generator will create you a default ``urls.py`` to match the View format you are using.

----------------------------
ViewSet & ModeViewSet Routes
----------------------------

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

A full application built with drf-generators can be found in the `tests directory <http://github.com/brobin/drf-generators/tree/master/tests>`_. Instructions on running the tests can be found in the test project's README.


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

.. |travis| image:: https://img.shields.io/travis/Brobin/drf-generators.svg?style=flat-square
    :target: https://travis-ci.org/Brobin/drf-generators/
    :alt: Travis CI

.. |django| image:: https://img.shields.io/badge/Django-1.7, 1.8-orange.svg?style=flat-square
    :target: http://djangoproject.com/
    :alt: Django 1.7, 1.8

.. |drf| image:: https://img.shields.io/badge/DRF-3.0, 3.1-orange.svg?style=flat-square
    :target: http://www.django-rest-framework.org/
    :alt: DRF 3.0, 3.1
