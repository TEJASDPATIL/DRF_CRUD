from django.db import models

class ProductModel(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    qty = models.IntegerField()