
from rest_framework.test import APITestCase


class PostAPITest(APITestCase):

    def set_up(self):
        url = '/api/v1/post/'
        data = {"title": "Test Post", "slug": "test", "content": "test"}
        response = self.client.post(url, data, format='json')
        return (response, data)

    def test_create_post(self):
        response, data = self.set_up()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["slug"], data["slug"])
        self.assertEqual(response.data["content"], data["content"])

    def test_list_post(self):
        self.set_up()
        url = '/api/v2/post'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_post(self):
        self.set_up()
        url = '/api/v1/post/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Test Post")

    def test_update_post(self):
        self.set_up()
        url = '/api/v1/post/1/'
        data = {"title": "Test Post", "slug": "test", "content": "Test"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["content"], data["content"])

    def test_delete_post(self):
        self.set_up()
        url = '/api/v1/post/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
