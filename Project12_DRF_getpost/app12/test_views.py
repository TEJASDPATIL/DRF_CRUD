import requests
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
import json
from rest_framework.test import APITestCase

import pytest
pytestmark = pytest.mark.django_db
from mixer.backend.django import mixer
from app12.models import ProductModel

class TestProductApiView(TestCase):
    def setUp(self):
        self.client = APIClient()
        print("client",self.client)
    def test_product_list(self):
        Product = mixer.blend(ProductModel,name="Cannon Camera")
        response = self.client.get("http://127.0.0.1:8000/list/")
        print(response.status_code)
        assert response.json != None
        assert len(response.json()) == 1
        assert response.status_code == 200

    def test_create_product_success(self):
        data = {
                "no": 102,
                "name": "Apple",
                "price": 25000,
                "qty": 4
                }
        response = self.client.post("http://127.0.0.1:8000/create/",data=data)
        assert response.json() != None
        assert response.status_code == 201
        assert ProductModel.objects.count() == 1

    def test_create_product_price_str(self):
        data = {
                "no": 102,
                "name": "Apple",
                "price": "sadd",
                "qty": 4
                }
        response = self.client.post("http://127.0.0.1:8000/create/",data=data)
        assert response.json() != None
        assert response.status_code == 400

    def test_create_product_qty_negative(self):
        data = {
                "no": 102,
                "name": "Apple",
                "price": "sadd",
                "qty": -4
                }
        response = self.client.post("http://127.0.0.1:8000/create/",data=data)
        assert response.json() != None
        assert response.status_code == 400

    def test_product_detail_api_success(self):
        Product = mixer.blend(ProductModel,no=101)
        response = self.client.get("http://127.0.0.1:8000/detail/101/")
        # assert response.json() != None
        assert response.status_code == 200

    def test_product_detail_api_fail(self):
        Product = mixer.blend(ProductModel,no=101)
        response = self.client.get("http://127.0.0.1:8000/detail/") #without Providing no in url
        # assert response.json() != None
        assert response.status_code == 404

    def test_product_delete_success(self):
        product = mixer.blend(ProductModel,no=101)
        response = self.client.delete("http://127.0.0.1:8000/delete/101/")
        print("STATUS",response.status_code)

        assert response.status_code == 204
    def test_product_delete_fail(self):
        product = mixer.blend(ProductModel,no=101)
        response = self.client.delete("http://127.0.0.1:8000/delete/102/")
        print("STATUS",response.status_code)

        assert response.status_code == 404

# class TestProduct(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         print("self.client",self.client)
    # def test_get_valid_url(self):
    #     user = mixer.blend(ProductModel,no=101)
    #
    #     url = 'http://127.0.0.1:8000/product/'
    #     # print("url",url)
    #     response = self.client.get(url)
    #     print(response.status_code)
    #     assert response.status_code == 200
    # def test_post_valid_data(self):
    #     p = mixer.blend(ProductModel,no=104,name ="apple",price=65475,qty=5)
    #     url = 'http://127.0.0.1:8000/product/'
    #     response = self.client.post(url)
    #     print("status::",response.status_code)
    #     assert response.status_code == 200
    #
    # def test_post_invalid_data(self):
    #     p = mixer.blend(ProductModel,no="as",name ="apple",price=65475,qty=5)
    #     url = 'http://127.0.0.1:8000/product/'
    #     response = self.client.post(url)
    #     print("status::",response.status_code)
    #
    #     assert response.status_code == 400
    # def test_string_in_no_qty(self):
    #     p = mixer.blend(ProductModel,no=144)
    #     res = ProductModel.objects.last()
    #     self.assertEqual(res.no,144)
        # url = 'http://127.0.0.1:8000/product/'
        # response = self.client.put(url)
        # print("status:", response.status_code)
        # assert response.status_code == 500


    #
    # def test_delete(self):
    #     url = 'http://127.0.0.1:8000/p' #incorrect url
    #     response = self.client.delete(url)
    #     print("status:", response.status_code)
    #     assert response.status_code == 404






