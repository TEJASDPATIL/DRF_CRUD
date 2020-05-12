from django.test import TestCase
from .models import ProductModel

class TestModels(TestCase):
    # def setUp(self):
    #     p = ProductModel.objects.create(
    #         no=105,name="Redmi",price=4545,qty=4
    #     )

    def test_product_creation(self):
        p = ProductModel.objects.create(
            no=105, name="Redmi", price=4545, qty=4
        )
        p_result = ProductModel.objects.last()
        assert p_result.no == 105

    def test_model_str_return(self):
        p = ProductModel.objects.create(
            no=105, name="Redmi", price=4545, qty=4
        )
        p_result = ProductModel.objects.last()
        assert str(p_result.name) == 'Redmi'