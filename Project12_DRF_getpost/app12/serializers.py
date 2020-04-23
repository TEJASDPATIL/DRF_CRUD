from rest_framework import serializers
from .models import ProductModel

class ProductSerializers(serializers.Serializer):
    no = serializers.IntegerField(min_value=101)
    name = serializers.CharField(max_length=30)
    price = serializers.FloatField(min_value=1000)
    qty = serializers.IntegerField(min_value=1)

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.no = validated_data.get("no",instance.no)
        instance.name = validated_data.get("name",instance.name)
        instance.price = validated_data.get("price",instance.price)
        instance.qty = validated_data.get("qty",instance.qty)
        instance.save()
        return instance