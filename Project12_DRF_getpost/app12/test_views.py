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

class TestProduct(TestCase):
    def setUp(self):
        self.client = APIClient()
        print("self.client",self.client)
    def test_ProductOperations(self):
        user = mixer.blend(ProductModel,no=101)

        url = 'http://127.0.0.1:8000/product/'
        # print("url",url)
        response = self.client.get(url)
        print(response.status_code)
        assert response.status_code == 200
    def test_post(self):
        p = mixer.blend(ProductModel,no=104,name ="apple",price=0,qty=5)
        url = 'http://127.0.0.1:8000/product/'
        response = self.client.post(url)
        print("status::",response.status_code)
        assert response.status_code == 400

    def test_put(self):
        p = mixer.blend(ProductModel,no=104,name =545555,price=0,qty="sghh")
        url = 'http://127.0.0.1:8000/product/'
        response = self.client.put(url)
        print("status:", response.status_code)
        assert response.status_code == 400
    def test_delete(self):
        url = 'http://127.0.0.1:8000/p' #incorrect url
        response = self.client.put(url)
        print("status:", response.status_code)
        assert response.status_code == 200






