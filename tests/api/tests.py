
from rest_framework.test import APITestCase
from django.core.management import call_command
from django.core.management.base import CommandError


class BaseTestCase(APITestCase):

    def init_data(self):
        self.url = '/api/post/'
        self.good_url = '/api/post/1'
        self.good_data = {"title": "Test", "slug": "test", "content": "test"}
        self.bad_url = '/api/post/15'
        self.bad_data = {"bad_data": 69, "slug": "test", "content": "Test"}

    def generate_api(self, format):
        args = ['api']
        opts = {'format': format, 'force': True}
        call_command('generate', *args, **opts)
        self.init_data()

    def set_up(self):
        response = self.client.post(self.url, self.good_data, format='json')
        return (response, self.good_data)

    def create_post(self):
        response, data = self.set_up()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["slug"], data["slug"])
        self.assertEqual(response.data["content"], data["content"])

    def create_post_error(self):
        response = self.client.post(self.url, self.bad_data, format='json')
        self.assertEqual(response.status_code, 400)

    def list_post(self):
        self.set_up()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def retrieve_post(self):
        self.set_up()
        response = self.client.get(self.good_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Test")

    def retrieve_post_error(self):
        response = self.client.get(self.bad_url)
        self.assertEqual(response.status_code, 404)

    def update_post(self):
        self.set_up()
        response = self.client.put(self.good_url, self.good_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["content"], self.good_data["content"])

    def update_post_error(self):
        response = self.client.put(self.bad_url, self.good_data, format='json')
        self.assertEqual(response.status_code, 404)
        self.set_up()
        response = self.client.put(self.good_url, self.bad_data, format='json')
        self.assertEqual(response.status_code, 400)

    def delete_post(self):
        self.set_up()
        response = self.client.delete(self.good_url)
        self.assertEqual(response.status_code, 204)

    def delete_post_error(self):
        response = self.client.delete(self.good_url)
        self.assertEqual(response.status_code, 404)

    def run_tests(self, type):
        print('\nTesting {} API'.format(type))
        self.generate_api(type)
        self.create_post()
        self.create_post_error()
        self.list_post()
        self.retrieve_post()
        self.retrieve_post_error()
        self.update_post()
        self.update_post_error()
        self.delete_post()
        self.delete_post_error()


class APIViewTest(BaseTestCase):

    def test_apiview(self):
        self.run_tests('apiview')


class FunctionViewTest(BaseTestCase):

    def test_function(self):
        self.run_tests('function')


class ViewSetTest(BaseTestCase):

    def test_viewset(self):
        self.run_tests('viewset')


class ModelViewSetTest(BaseTestCase):

    def test_modelviewset(self):
        self.run_tests('modelviewset')


class EdgeCaseTest(BaseTestCase):

    def test_invalid_format(self):
        try:
            self.generate_api('asdf')
        except Exception as e:
            self.assertTrue(isinstance(e, CommandError))

