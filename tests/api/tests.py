
from rest_framework.test import APITestCase
from django.core.management import call_command


class BaseTestCase(APITestCase):

    def generate_api(self, format):
        args = ['api']
        opts = {'format': format, 'force': True}
        call_command('generate', *args, **opts)

    def set_up(self):
        url = '/api/post/'
        data = {"title": "Test Post", "slug": "test", "content": "test"}
        response = self.client.post(url, data, format='json')
        return (response, data)

    def create_post(self):
        response, data = self.set_up()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["slug"], data["slug"])
        self.assertEqual(response.data["content"], data["content"])

    def list_post(self):
        self.set_up()
        url = '/api/post/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def retrieve_post(self):
        self.set_up()
        url = '/api/post/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Test Post")

    def update_post(self):
        self.set_up()
        url = '/api/post/1'
        data = {"title": "Test Post", "slug": "test", "content": "Test"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["content"], data["content"])

    def delete_post(self):
        self.set_up()
        url = '/api/post/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)


class APIViewTest(BaseTestCase):

    def test_apiview_create(self):
        print('\nTesting APIView API')
        self.generate_api('apiview')
        self.create_post()

    def test_apiview_list(self):
        self.list_post()

    def test_apiview_retrieve(self):
        self.retrieve_post()

    def test_apiview_update(self):
        self.update_post()

    def test_apiview_delete(self):
        self.delete_post()


class FunctionViewTest(BaseTestCase):

    def test_function_create(self):
        print('\nTesting function API')
        self.generate_api('function')
        self.create_post()

    def test_function_list(self):
        self.list_post()

    def test_function_retrieve(self):
        self.retrieve_post()

    def test_function_update(self):
        self.update_post()

    def test_function_delete(self):
        self.delete_post()


class ViewSetTest(BaseTestCase):

    def test_viewset_create(self):
        print('\nTesting ViewSet API')
        self.generate_api('viewset')
        self.create_post()

    def test_viewset_list(self):
        self.list_post()

    def test_viewset_retrieve(self):
        self.retrieve_post()

    def test_viewset_update(self):
        self.update_post()

    def test_viewset_delete(self):
        self.delete_post()


class ModelViewSetTest(BaseTestCase):

    def test_modelviewset_create(self):
        print('\nTesting ModelViewSet API')
        self.generate_api('modelviewset')
        self.create_post()

    def test_modelviewset_list(self):
        self.list_post()

    def test_modelviewset_retrieve(self):
        self.retrieve_post()

    def test_modelviewset_update(self):
        self.update_post()

    def test_modelviewset_delete(self):
        self.delete_post()
