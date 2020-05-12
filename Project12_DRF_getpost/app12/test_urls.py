from django.urls import reverse,resolve
from django.test import SimpleTestCase
from .views import ProductListView,ProductCreateApiView,ProductDetailApiView,ProductDeleteApiView

class TestUrls(SimpleTestCase):
    def test_list_url(self):
        url = reverse('list_products')
        print(resolve(url))
        assert resolve(url).func.view_class == ProductListView

    def test_create_url(self):
        url = reverse('create')
        print(resolve(url))
        assert resolve(url).func.view_class == ProductCreateApiView

    def test_detail_url(self):
        url = reverse('detail',args=['102'])
        print(resolve(url))
        assert resolve(url).func.view_class == ProductDetailApiView

    def test_delete_url(self):
        url = reverse('delete',args=['101'])
        print(resolve(url))
        assert resolve(url).func.view_class == ProductDeleteApiView
