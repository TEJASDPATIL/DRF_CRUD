#from django.test import TestCase

from rest_framework.test import APITestCase


from .models import ProductModel

class ProductAPITest(APITestCase):
    def setUp(self):
        ProductModel.objects.create(no=101,name="iPhone",price=90000.00,qty=1)
        print("Setup Method")
    def test_get_method(self):
        url = "http://127.0.0.1:8000/product/"
        response = self.client.get(url)
        print(response.status_code)
        self.assertEqual(response.status_code,200)
        print("test1")
    def test_post_method_success(self):
        print("Test method")
        url = "http://127.0.0.1:8000/product/"
        data = {
            "no":103,"name":"Redmi","price":17000.00,"qty":5
        }
        response = self.client.post(url,data,format="json")
        print(response.status_code)
        self.assertEqual(response.status_code,200)
        print("test2")
    def test_post_method_fail(self):
        print("Test method")
        url = "http://127.0.0.1:8000/product/"
        data = {
            "no":103,"name":"Redmi"
        }
        response = self.client.post(url,data,format="json")
        print(response.status_code)
        self.assertEqual(response.status_code,400)
        print("test3")
    def test_put_method_success(self):
        print("Test Put method")
        url = "http://127.0.0.1:8000/product/"
        data = {
            "no": 103, "name": "Redmi"
        }
        response = self.client.put(url, data, format="json")
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_put_method_fail(self):
        print("Test Put method Fail")
        url = "http://127.0.0.1:8000/product/"
        data = {
            "no": 106, "name": "Redmi"
        }
        response = self.client.put(url, data, format="json")
        print(response.status_code)
        self.assertEqual(response.status_code, 400)

    def test_delete_success(self):
        print("Test delete method Success")
        url = "http://127.0.0.1:8000/product/"
        response = self.client.delete(url)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
    def test_delete_Fail(self):
        print("Test delete method Fail")
        url = "http://127.0.0.1:8000/produc/"
        response = self.client.delete(url)
        print(response.status_code)
        self.assertEqual(response.status_code, 400)


