from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase

from rest_framework.test import APITestCase

from .models import Post


class BaseTestCase(APITestCase):

    def setUp(self):
        self.url = '/api/post/'
        self.good_data = {"title": "Test", "slug": "test", "content": "test"}
        post = Post.objects.create(**self.good_data)
        self.good_url = '/api/post/{0}/'.format(post.id)
        self.bad_url = '/api/post/15/'
        self.bad_data = {"bad_data": 69, "slug": "test", "content": "Test"}

    def test_create_post(self):
        response = self.client.post(self.url, self.good_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], self.good_data["title"])
        self.assertEqual(response.data["slug"], self.good_data["slug"])
        self.assertEqual(response.data["content"], self.good_data["content"])

    def test_create_post_error(self):
        response = self.client.post(self.url, self.bad_data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_list_post(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_post(self):
        response = self.client.get(self.good_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Test")

    def test_retrieve_post_error(self):
        response = self.client.get(self.bad_url)
        self.assertEqual(response.status_code, 404)

    def test_update_post(self):
        response = self.client.put(self.good_url, self.good_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["content"], self.good_data["content"])

    def test_update_post_error(self):
        response = self.client.put(self.bad_url, self.good_data, format='json')
        self.assertEqual(response.status_code, 404)
        response = self.client.put(self.good_url, self.bad_data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_delete_post(self):
        response = self.client.delete(self.good_url)
        self.assertEqual(response.status_code, 204)

    def test_delete_post_error(self):
        response = self.client.delete(self.bad_url)
        self.assertEqual(response.status_code, 404)


class GeneratorsTestCase(TestCase):

    def test_invalid_format(self):
        try:
            args = ['api']
            opts = {'format': 'asdf', 'force': True}
            call_command('generate', *args, **opts)
        except Exception as e:
            self.assertTrue(isinstance(e, CommandError))
