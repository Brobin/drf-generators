
# Test API

This folder contains a test Django Rest Framework project featuring API Views, Serializers and Urls generated using drf-generators.

| api_v1 | ViewSet based Views and routes |
| api_v2 | APIView style views and standard urls |

Each app has 5 tests to test the basic functionality of the View, Serializers and Urls for the provided model (Post).

| `test_create_post` | Tests creating a Post object |
| `test_list_post` | Tests gettin a list of Post objects |
| `test_retrieve_post` | Tests geting a Post object |
| `test_update_post` | Tests updating a Post object |
| `test_delete_post` | Tests deleting a Post object |

To run the tests on both applications, simply type the following command:

```bash
python manage.py test
```

That's it!
